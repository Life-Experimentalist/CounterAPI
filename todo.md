# 📋 TODO - ProjectCounter

## ✅ MVP Done
- [x] GET /projects
- [x] POST /ping/{name}
- [x] Add project
- [x] Edit project
- [x] Delete project
- [x] SQLite persistence
- [x] Deployable via Render

## 🔜 Next Improvements
- [ ] Add `/health` endpoint for UptimeRobot
- [ ] Add total count summary to `/projects`
- [ ] Add `created_at`, `updated_at` fields
- [ ] Add project rename history
- [ ] Secure ping endpoint with optional token
- [ ] Add tests using `pytest`

## 🧪 Stretch Goals
- [ ] Export counters to CSV/JSON
- [ ] Backup counters.db to GitHub Actions daily
- [ ] Create self-host CLI deploy script