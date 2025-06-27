import os
import sqlite3
from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from database import get_db, init_db

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
init_db()

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
    return FileResponse("dashboard.html")


@app.get("/projects")
def get_projects():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT name, description, count FROM projects")
    return [{"name": n, "description": d, "count": c} for n, d, c in cursor.fetchall()]


@app.post("/projects")
def create_project(proj: ProjectBase):
    db = get_db()
    try:
        db.execute(
            "INSERT INTO projects (name, description) VALUES (?, ?)",
            (proj.name, proj.description),
        )
        db.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(400, f"Project already exists. See: {WIKI_URL}")
    return {"message": f"Project '{proj.name}' added"}


@app.put("/projects")
def update_project(body: ProjectUpdate, request: Request):
    name = request.query_params.get("name")
    if not name:
        raise HTTPException(400, f"Project name is required in query. See: {WIKI_URL}")

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT 1 FROM projects WHERE name = ?", (name,))
    if not cursor.fetchone():
        raise HTTPException(404, f"Project not found. See: {WIKI_URL}")

    if body.new_name:
        cursor.execute(
            "UPDATE projects SET name = ? WHERE name = ?", (body.new_name, name)
        )
    if body.description is not None:
        cursor.execute(
            "UPDATE projects SET description = ? WHERE name = ?",
            (body.description, body.new_name or name),
        )
    if body.count is not None:
        cursor.execute(
            "UPDATE projects SET count = ? WHERE name = ?",
            (body.count, body.new_name or name),
        )

    db.commit()
    return {"message": "Updated"}

@app.delete("/projects")
def delete_project(request: Request):
    name = request.query_params.get("name")
    if not name:
        raise HTTPException(400, f"Project name is required in query. See: {WIKI_URL}")

    db = get_db()
    db.execute("DELETE FROM projects WHERE name = ?", (name,))
    db.commit()
    return {"message": f"Deleted {name}"}

@app.post("/ping")
def ping_project(proj: ProjectPing):
    name = proj.name
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT OR IGNORE INTO projects (name) VALUES (?)", (name,))
    cursor.execute("UPDATE projects SET count = count + 1 WHERE name = ?", (name,))
    db.commit()
    return {"message": f"Ping received for {name}"}

@app.get("/meta")
def get_meta():
    return {
        "repo": REPO_SLUG,
        "wiki": WIKI_URL,
        "commit": RENDER_GIT_COMMIT,
        "branch": RENDER_GIT_BRANCH,
        "service": RENDER_SERVICE_NAME,
        "external_url": RENDER_EXTERNAL_URL,
    }
