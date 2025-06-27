# 🧱 Architecture - ProjectCounter

```mermaid
flowchart TD
    A[UI: index.html - GitHub Pages/Local] -- fetch --> B[API: FastAPI Backend]
    B -- stores data --> C[DB: SQLite counters.db]
    B -- hosted on --> D[Render Cloud]
```

## 🧩 Components Explained

- **GitHub Pages**: Hosts your static `index.html` UI.
- **FastAPI Backend**: Handles all `/projects`, `/ping`, CRUD endpoints.
- **SQLite (counters.db)**: Persistent local DB file used by backend.
- **Render**: Free cloud host that deploys FastAPI + SQLite service with automatic redeploy from GitHub.
