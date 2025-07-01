# 🧱 Architecture - CounterAPI

```mermaid
flowchart TD
    subgraph "Client-Side"
        A[UI: Dashboard (index.html)]
    end

    subgraph "Server-Side (Hosted on Render)"
        B[API: FastAPI Backend]
        C[DB: PostgreSQL (Filess.io or other cloud DB)]
    end

    A -- API Calls (fetch) --> B
    B -- Stores/Retrieves Data --> C
```

## 🧩 Components Explained

- **GitHub Pages / Render**: Hosts your static `index.html` UI.
- **FastAPI Backend**: Handles all `/projects`, `/ping`, CRUD endpoints.
- **PostgreSQL (Filess.io or other cloud DB)**: Persistent cloud database used by backend.
- **Render**: Free cloud host that deploys FastAPI + PostgreSQL service with automatic redeploy from GitHub.
