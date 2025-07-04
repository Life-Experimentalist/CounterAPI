# 📝 CounterAPI - To-Do List

This file tracks planned features and improvements for the CounterAPI project.

---

## ✅ Completed

- [x] Core API for CRUD and pinging projects with descriptions
- [x] PostgreSQL (Filess.io) database integration with schema support
- [x] Deployment setup for Render.com with environment variable configuration (no code changes needed)
- [x] Comprehensive `README.md` and usage documentation
- [x] Interactive frontend dashboard (`index.html`) for managing projects
- [x] Environment detection and auto-configuration for Render deployment
- [x] `/meta` endpoint for detailed deployment and database info
- [x] Beautiful glassmorphism UI with smooth animations and transitions
- [x] Real-time project statistics (total projects, visits, averages)
- [x] Debounced project reloading for seamless UI updates
- [x] Responsive mobile-friendly design
- [x] Settings modal with API configuration and connection testing
- [x] Database schema viewer showing tables, columns, and connection status
- [x] Dark Reader extension compatibility (disabled for consistent UI)
- [x] Proper error handling for database connection failures
- [x] Dynamic connection status based on actual database state

---

## 🎯 Next Up (Short-Term)

- [ ] **API Key Authentication**: Secure the API endpoints so that only authorized users can add, edit, or delete projects. Pinging can remain public.
- [ ] **SVG Badges**: Create a new endpoint `/projects/{name}/badge` that generates a dynamic SVG badge (like shields.io) displaying the current count. This is great for embedding in GitHub READMEs.
- [ ] **Enhanced Dashboard Stats**: Add a chart to the dashboard to show visit history for a selected project (e.g., last 7 days).

---

## 🚀 Future Ideas (Long-Term)

- [ ] **User Accounts**: Introduce a simple user system to allow different people to manage their own sets of projects.
- [ ] **Data Export**: Add an endpoint to export all project data to a CSV or JSON file.
- [ ] **Backend Logging**: Implement more robust logging on the backend for easier debugging.
- [ ] **FastAPI Auto-Docs**: Customize and expose the built-in FastAPI documentation (`/docs` and `/redoc`) for a more formal API reference.
- [ ] **More Granular Pinging**: Allow pings to include metadata (e.g., version, source) to track usage more granularly.
