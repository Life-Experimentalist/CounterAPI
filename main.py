import os
from typing import Optional

import psycopg2
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from psycopg2 import sql
from pydantic import BaseModel

from database import get_db

# GitHub Wiki fallback
REPO_SLUG = os.getenv("RENDER_GIT_REPO_SLUG", "Life-Experimentalist/CounterAPI")
WIKI_URL = os.getenv("REPO_WIKI", f"https://github.com/{REPO_SLUG}/wiki")

# Render deployment metadata
RENDER_GIT_COMMIT = os.getenv("RENDER_GIT_COMMIT", "unknown")
RENDER_SERVICE_ID = os.getenv("RENDER_SERVICE_ID", "unknown")
RENDER_SERVICE_NAME = os.getenv("RENDER_SERVICE_NAME", "unknown")
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL", "unknown")
RENDER_GIT_BRANCH = os.getenv("RENDER_GIT_BRANCH", "main")

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Models
class ProjectBase(BaseModel):
    name: str
    description: str = ""


class ProjectUpdate(BaseModel):
    new_name: Optional[str] = None
    description: Optional[str] = None
    count: Optional[int] = None


class ProjectPing(BaseModel):
    name: str


# Serve dashboard
@app.get("/")
def root():
    return FileResponse("index.html")


@app.get("/projects")
def get_projects():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT name, description, count FROM projects")
    projects = [
        {"name": n, "description": d, "count": c} for n, d, c in cursor.fetchall()
    ]
    cursor.close()
    db.close()
    return projects


@app.post("/projects")
def create_project(proj: ProjectBase):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO projects (name, description) VALUES (%s, %s)",  # Use %s for psycopg2
            (proj.name, proj.description),
        )
        db.commit()
        cursor.close()
        db.close()
        return {"message": f"Project '{proj.name}' created successfully"}

    # except sqlite3.IntegrityError: # Remove this line
    except (
        psycopg2.errors.UniqueViolation
    ):  # Add this line for PostgreSQL unique constraint error
        db.rollback()  # Rollback transaction on error
        cursor.close()
        db.close()
        raise HTTPException(
            status_code=400, detail=f"Project '{proj.name}' already exists"
        )
    except Exception as e:
        db.rollback()
        cursor.close()
        db.close()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@app.put("/projects")
def update_project(name: str, proj: ProjectUpdate):
    db = get_db()
    cursor = db.cursor()
    updates = []
    values = []

    if proj.new_name is not None:
        updates.append("name = %s")  # Use %s
        values.append(proj.new_name)
    if proj.description is not None:
        updates.append("description = %s")  # Use %s
        values.append(proj.description)
    if proj.count is not None:
        updates.append("count = %s")  # Use %s
        values.append(proj.count)

    if not updates:
        cursor.close()
        db.close()
        raise HTTPException(status_code=400, detail="No fields provided for update")

    values.append(name)  # Add the original name for the WHERE clause
    query = f"UPDATE projects SET {', '.join(updates)} WHERE name = %s"  # Use %s

    try:
        cursor.execute(query, values)
        db.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        db.close()

        if rows_affected == 0:
            raise HTTPException(status_code=404, detail=f"Project '{name}' not found")

        return {"message": f"Project '{name}' updated successfully"}

    except (
        psycopg2.errors.UniqueViolation
    ):  # Handle unique name constraint if new_name is provided
        db.rollback()
        cursor.close()
        db.close()
        raise HTTPException(
            status_code=400, detail=f"Project name '{proj.new_name}' already exists"
        )
    except Exception as e:
        db.rollback()
        cursor.close()
        db.close()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@app.delete("/projects/{name}")
def delete_project(name: str):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(
            "DELETE FROM projects WHERE name = %s", (name,)
        )  # Use %s, note the comma for tuple
        db.commit()
        rows_affected = cursor.rowcount
        cursor.close()
        db.close()

        if rows_affected == 0:
            raise HTTPException(status_code=404, detail=f"Project '{name}' not found")

        return {"message": f"Project '{name}' deleted successfully"}

    except Exception as e:
        db.rollback()
        cursor.close()
        db.close()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@app.post("/projects/ping")
def ping_project(proj: ProjectPing):
    db = get_db()
    cursor = db.cursor()
    try:
        # Ensure project exists before updating
        cursor.execute("SELECT name FROM projects WHERE name = %s", (proj.name,))
        if cursor.fetchone() is None:
            cursor.close()
            db.close()
            raise HTTPException(
                status_code=404, detail=f"Project '{proj.name}' not found"
            )
        cursor.execute(
            "UPDATE projects SET count = count + 1 WHERE name = %s RETURNING name, count",
            (proj.name,),
        )
        result = cursor.fetchone()
        db.commit()
        cursor.close()
        db.close()

        if result is None:
            raise HTTPException(
                status_code=404,
                detail=f"Project '{proj.name}' not found or update failed",
            )
        name, count = result
        return {"name": name, "count": count}

    except Exception as e:
        db.rollback()
        cursor.close()
        db.close()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


# Endpoint to get deployment and database info
@app.get("/meta")
def meta_info(request: Request):
    db = get_db()
    cursor = db.cursor()
    # Get all tables
    cursor.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
    )
    tables = [row[0] for row in cursor.fetchall()]
    db_info = {
        "db_host": os.getenv("DB_HOST"),
        "db_port": os.getenv("DB_PORT"),
        "db_name": os.getenv("DB_NAME"),
        "db_user": os.getenv("DB_USER"),
        "tables": {},
    }
    for table in tables:
        # Get columns
        cursor.execute(
            "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = %s",
            (table,),
        )
        columns = cursor.fetchall()
        # Get row count (safe SQL identifier)
        cursor.execute(
            sql.SQL("SELECT COUNT(*) FROM {} ").format(sql.Identifier(table))
        )
        row = cursor.fetchone()
        row_count = row[0] if row else 0
        db_info["tables"][table] = {
            "columns": [{"name": c[0], "type": c[1]} for c in columns],
            "row_count": row_count,
        }
    cursor.close()
    db.close()
    # Merge deployment info
    deployment_info = {
        "service_name": RENDER_SERVICE_NAME,
        "service_id": RENDER_SERVICE_ID,
        "external_url": RENDER_EXTERNAL_URL,
        "git_branch": RENDER_GIT_BRANCH,
        "git_commit": RENDER_GIT_COMMIT,
        "wiki_url": WIKI_URL,
        "cors_allow_origins": request.app.middleware[0].options.get("allow_origins"),
    }
    return {"deployment": deployment_info, "database": db_info}
