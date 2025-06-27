Here's a list of `curl` commands you can use to interact with your CounterAPI backend (hosted on Render, e.g. `https://yourname.onrender.com`). Replace `https://yourname.onrender.com` with your actual API base if different.

---

### ✅ 1. **Get all projects**

```bash
curl https://yourname.onrender.com/projects
```

---

### ✅ 2. **Add a new project**

```bash
curl -X POST https://yourname.onrender.com/projects \
  -H "Content-Type: application/json" \
  -d '{"name": "MyNewProject", "description": "An optional project description"}'
```

---

### ✅ 3. **Ping a project (increment count)**

```bash
curl -X POST https://yourname.onrender.com/ping/MyNewProject
```

---

### ✅ 4. **Edit (rename/describe) a project**

```bash
curl -X PUT https://yourname.onrender.com/projects/MyNewProject \
  -H "Content-Type: application/json" \
  -d '{"new_name": "MyRenamedProject", "description": "Updated description"}'
```

---

### ✅ 5. **Delete a project**

```bash
curl -X DELETE https://yourname.onrender.com/projects/MyRenamedProject
```

---

Let me know if you'd like a shell script that auto-generates these or you want Postman collection JSON too.
