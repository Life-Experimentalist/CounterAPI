# 📊 CounterAPI

**CounterAPI** is a fully self-hosted API service to track how many times your projects are used.
Powered by **FastAPI** and **SQLite**, it's ideal for hobby projects, dev dashboards, or lightweight analytics.

---

## 🌟 Features

* 🔁 Track project usage with simple HTTP pings
* 🧓 View all counters in a clean JSON format
* 🛠️ Full CRUD: Add, edit, rename, or delete projects
* 📂 Persistent storage using SQLite (file-based)
* 🚀 One-click deploy to Render (completely free)
* 🧪 Comes with Postman Collection for quick testing
* 🛡️ Automatically configures GitHub Wiki fallback for docs

---

## 🧐 Architecture Overview

* **Frontend (optional)**: Single-page UI served from Render (index.html)
* **Backend**: FastAPI app handling all API routes
* **Database**: Local SQLite (`counters.db`)
* **Hosting**: [Render.com](https://render.com) (Free tier)
* **Deployment**: Done via `render.yaml` auto-detected during setup

---

## 🚀 Getting Started

### 1. 🔁 Fork This Repo

Click the [Fork button](https://github.com/Life-Experimentalist/CounterAPI/fork) and clone it locally:

```bash
git clone https://github.com/your-username/CounterAPI.git
cd CounterAPI
```

---

### 2. 🧪 Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the dev server:

```bash
uvicorn main:app --reload
```

Now open: [http://localhost:8000/projects](http://localhost:8000/projects)

---

### 3. 🌐 Deploy on Render (One Click)

Just click this button:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Life-Experimentalist/CounterAPI)

Render will:

* Detect `render.yaml`
* Ask for a **custom web service name** (e.g. `yourname-counterapi`)
* Deploy it with persistent SQLite database

Once deployed, your base URL will be:

```
https://<your-custom-name>.onrender.com
```

---

## 📡 API Reference

### ➕ Add Project

```http
POST /projects
{
  "name": "my-cool-app",
  "description": "My test project"
}
```

### ✏️ Update Project

```http
PUT /projects
{
  "name": "my-cool-app",
  "new_name": "my-updated-app",
  "description": "Updated desc"
}
```

### ❌ Delete Project

```http
DELETE /projects
{
  "name": "my-cool-app"
}
```

### 📈 Ping (Increment Count)

```http
POST /ping
{
  "name": "my-cool-app"
}
```

### 📊 List All Projects

```http
GET /projects
```

All endpoints return a JSON response.
If a project is not found, a helpful error message with a link to the Wiki is returned automatically.

---

## 📂 Project Structure

```
CounterAPI/
├── main.py              # FastAPI logic
├── database.py          # SQLite setup
├── requirements.txt     # Python dependencies
├── render.yaml          # Render deployment descriptor
├── index.html           # UI frontend (served by backend)
├── architecture.md      # Mermaid diagrams + explanations
├── todo.md              # Planned roadmap
└── counters.db          # SQLite file (auto-created)
```

---

## 📄 .env Variables for Render

No `.env` is required unless you want to override defaults.

Optional environment variables:

| Name                   | Description                                    |
| ---------------------- | ---------------------------------------------- |
| `RENDER_GIT_REPO_SLUG` | Auto-detected by Render (used for error links) |
| `RENDER_EXTERNAL_URL`  | Auto-detected public API base URL              |

---

## 🧪 Postman

We provide a ready-made Postman collection to test all endpoints.

### 📥 How to Use

1. [Download `CounterAPI.postman_collection.json`](./postman/CounterAPI.postman_collection.json)
2. Change the `base_url` at the bottom of the file from:
3. Open [Postman](https://www.postman.com/)
4. Click **Import → Upload Files** → Select the JSON file
5. After import, **go to the "Variables" tab** inside the collection

```
https://projectcounter.onrender.com
```

to **your own deployed URL**, such as:

```
https://your-custom-name.onrender.com
```

Now you're ready to test all API routes directly! ✅

---

## 🔧 Tech Stack

* 🐍 Python 3.x
* ⚡ FastAPI
* 📓 SQLite
* ☁️ Render.com

---

## 📄 License

Apache 2.0 – Free for personal, educational, and commercial use.

---

## 🙋‍♀️ Contributing

This project is forkable and beginner-friendly.
Feel free to tweak, star, or fork it to build your own tracker!

---
