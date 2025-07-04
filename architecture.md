# 🧱 Architecture - CounterAPI

```mermaid
flowchart TD
    subgraph "Client-Side"
        A[Interactive Dashboard<br/>index.html]
        A1[Real-time Stats]
        A2[Project Management]
        A3[Settings & Config]
        A4[Database Viewer]
    end

    subgraph "Server-Side (Render)"
        B[FastAPI Backend<br/>main.py]
        B1[CRUD Operations]
        B2[Ping Tracking]
        B3[Meta Info API]
        B4[Health Check API]
        B5[Static File Serving]
    end

    subgraph "Database (Cloud)"
        C[PostgreSQL<br/>Filess.io or similar]
        C1[Projects Table]
        C2[Schema Support]
    end

    A -- API Calls --> B
    A1 -.-> B1
    A2 -.-> B1
    A2 -.-> B2
    A3 -.-> B3
    A3 -.-> B4
    A4 -.-> B3

    B -- Database Queries --> C
    B1 -.-> C1
    B2 -.-> C1
    B3 -.-> C2
    B4 -.-> C2
    B5 -.-> A
```

## 🧩 Components Explained

- **Interactive Dashboard**: Modern single-page application with glassmorphism design, real-time stats, and seamless updates
- **FastAPI Backend**: Handles all API endpoints including CRUD operations, ping tracking, health checks, and deployment metadata
- **PostgreSQL Database**: Cloud-hosted database (Filess.io recommended) with schema support and table introspection
- **Render Deployment**: Free cloud hosting with automatic deployment, environment detection, and static file serving
- **Health Check System**: Real-time database connectivity testing with proper status reporting
