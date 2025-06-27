import sqlite3
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# from models import Project
from pydantic import BaseModel

from database import get_db, init_db

app = FastAPI()
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ProjectBase(BaseModel):
    name: str
    description: str = ""


class ProjectUpdate(BaseModel):
    new_name: Optional[str] = None
    description: Optional[str] = None


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
        raise HTTPException(400, "Project already exists")
    return {"message": f"Project '{proj.name}' added"}


@app.put("/projects/{name}")
def update_project(name: str, upd: ProjectUpdate):
    db = get_db()
    cursor = db.cursor()
    if upd.new_name:
        cursor.execute(
            "UPDATE projects SET name = ? WHERE name = ?", (upd.new_name, name)
        )
    if upd.description is not None:
        cursor.execute(
            "UPDATE projects SET description = ? WHERE name = ?",
            (upd.description, upd.new_name or name),
        )
    db.commit()
    return {"message": "Updated"}


@app.delete("/projects/{name}")
def delete_project(name: str):
    db = get_db()
    db.execute("DELETE FROM projects WHERE name = ?", (name,))
    db.commit()
    return {"message": f"Deleted {name}"}


@app.post("/ping/{name}")
def ping_project(name: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT OR IGNORE INTO projects (name) VALUES (?)", (name,))
    cursor.execute("UPDATE projects SET count = count + 1 WHERE name = ?", (name,))
    db.commit()
    return {"message": f"Ping received for {name}"}
