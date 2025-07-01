# 📖 CounterAPI - Quick Usage Guide

This guide provides quick curl/API examples for using your deployed CounterAPI instance.

---

## ➕ Add a New Project

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "my-cool-app", "description": "An example project"}' \
  https://<your-api-url>/projects
```

## 📈 Ping (Increase Count)

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "my-cool-app"}' \
  https://<your-api-url>/projects/ping
```

## 📊 Get All Projects

```bash
curl https://<your-api-url>/projects
```

## 🗑️ Delete a Project

```bash
curl -X DELETE https://<your-api-url>/projects/my-cool-app
```

## 🛠️ Update a Project

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"new_name": "my-renamed-app", "description": "Updated description"}' \
  "https://<your-api-url>/projects?name=my-cool-app"
```

## 🧬 View Database Meta Info

```bash
curl https://<your-api-url>/meta
```

---

Replace `<your-api-url>` with your deployed Render URL (e.g., `https://yourname-counterapi.onrender.com`).
