# 📊 ProjectCounter

**ProjectCounter** is a self-hosted API service to track how many times your projects are used.
Built with **FastAPI** and **SQLite**, and deployable for free on **Render**, it's perfect for hobby projects or developer dashboards.

---

## 🌟 Features

- ✅ Track individual project usage with simple pings
- ✅ View all projects and their counters
- ✅ CRUD support: add, edit, delete projects
- ✅ Persistent storage with SQLite (file-based)
- ✅ No external DBs or paid hosting required
- ✅ Deploy once and forget — works even after cold starts

---

## 🚀 Get Started

### 1. 🧬 Fork or Clone the Repo

```bash
git clone https://github.com/Life-Experimentalist/ProjectCounter.git
cd ProjectCounter
```

### 2. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. 🧪 Run Locally (for development)

```bash
uvicorn main:app --reload
```

### 4. 🌐 Deploy on Render (Free Tier)

* Go to [https://render.com](https://render.com)
* Click **New Web Service**
* Connect your GitHub → Select `ProjectCounter` repo
* It will auto-detect `render.yaml` and deploy

Done! You now have a public API like:

```
GET    /projects
POST   /projects
PUT    /projects/{name}
DELETE /projects/{name}
POST   /ping/{project}
```

---

## 🔗 Example API Usage

### ➕ Add a new project

```http
POST /projects
{
  "name": "my-cool-app",
  "description": "An example project"
}
```

### 📈 Ping (increase count)

```http
POST /ping/my-cool-app
```

### 📊 Get all projects

```http
GET /projects
```

---

## 🧾 Todo / Roadmap

See [`todo.md`](./todo.md)

---

## 🧩 Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/) - backend framework
* [SQLite](https://www.sqlite.org/index.html) - lightweight embedded database
* [Render](https://render.com/) - free cloud hosting
* [GitHub Pages](https://pages.github.com/) - static site hosting

---

## 🛡️ License

Apache 2.0 — Free for personal or commercial use.

---

## 🙋 Contributing

This project is designed for hobby use and easy duplication.
Feel free to fork, improve, or adapt for your own portfolio!

---

## 📂 Project Structure

```
ProjectCounter/
├── main.py              # FastAPI backend
├── database.py          # DB init logic
├── models.py            # SQLite table schema
├── requirements.txt     # Dependencies
├── render.yaml          # Render deployment config
├── .gitignore           # Ignore counters.db
├── counters.db          # Auto-generated SQLite file
├── index.html           # Frontend UI (can be GitHub Pages)
├── README.md            # Setup instructions
├── architecture.md      # System architecture (Mermaid + text)
└── todo.md              # Roadmap + future features
```

🛠️ **Note for Forkers and Contributors**
When deploying to Render, you'll be asked to provide a unique service name. Make sure to enter something custom like `yourname-projectcounter` to avoid name collisions.
