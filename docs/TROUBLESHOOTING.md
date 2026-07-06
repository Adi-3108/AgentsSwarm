# Troubleshooting Guide

## 1. Common Installation Issues on Windows

### chroma-hnswlib fails to build
**Symptom:** `ERROR: Failed building wheel for chroma-hnswlib`  
**Cause:** Missing Microsoft Visual C++ Build Tools.  
**Fix:** Download and install [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

### numpy fails to build from source
**Symptom:** `ERROR: NumPy requires GCC >= 8.4`  
**Cause:** pip is trying to compile numpy from source on an unsupported Python version (e.g. Python 3.13).  
**Fix:** Use Python 3.12 where a binary wheel is available. Run:
```powershell
py -3.12 -m venv backend/venv
```

### crewai version not found
**Symptom:** `No matching distribution found for crewai==0.41.1`  
**Cause:** The version was removed from PyPI.  
**Fix:** Use Python 3.12 venv; the version resolves correctly on that interpreter.

---

## 2. Redis / ChromaDB Connectivity

### Redis connection refused
**Fix:** Start Redis via Docker Compose:
```bash
docker-compose -f docker-compose.dev.yml up -d redis
```

### ChromaDB rejects requests
**Fix:** Ensure ChromaDB container is healthy:
```bash
docker-compose -f docker-compose.dev.yml up -d chromadb
```

---

## 3. Firebase Auth Errors
**Symptom:** `401 Unauthorized` on API endpoints.  
**Fix:** Verify `FIREBASE_PROJECT_ID`, `SUPABASE_JWT_SECRET` are correctly set in `.env`.

---

## 4. WebSocket Approval Gate Not Firing
**Symptom:** Task hangs at executor approval step.  
**Fix:** Ensure the React dashboard is connected to the correct WebSocket URL (`ws://localhost:8000/ws/{run_id}`).
