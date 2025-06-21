Installing Redis on **Windows** is slightly different because Redis is natively developed for **Linux/Unix** systems. However, you can run Redis on Windows in the following ways:

---

## ✅ Recommended Method: **Install Redis using WSL (Windows Subsystem for Linux)**

### 🔧 Step-by-Step:

1. **Enable WSL** (if not already done):

   * Open PowerShell as Administrator:

     ```bash
     wsl --install
     ```
   * Restart your system when prompted.

2. **Install Ubuntu from Microsoft Store**:

   * Open Microsoft Store → Search for **"Ubuntu"** → Install any latest version (e.g., Ubuntu 22.04 LTS).

3. **Open Ubuntu terminal** and install Redis:

   ```bash
   sudo apt update
   sudo apt install redis-server
   ```

4. **Start Redis server**:

   ```bash
   sudo service redis-server start
   ```

5. **Test Redis is working**:

   ```bash
   redis-cli
   127.0.0.1:6379> SET name "Redis"
   127.0.0.1:6379> GET name
   ```

---

## 🧪 Alternative (Not Recommended for Production): **Memurai or Redis for Windows binaries**

### 🅰️ Option 1: Memurai (Redis-compatible server for Windows)

1. Go to: [https://www.memurai.com/download](https://www.memurai.com/download)
2. Download the **Memurai Developer Edition**.
3. Install and run it – it works like a Redis server.
4. Connect using `redis-cli` or from any Redis client.

---

### 🅱️ Option 2: Microsoft Archived Redis Binaries

Microsoft used to maintain a Windows port of Redis (no longer maintained).

1. Visit: [https://github.com/microsoftarchive/redis/releases](https://github.com/microsoftarchive/redis/releases)
2. Download the latest `.msi` or `.zip` file (e.g., `Redis-x64-3.2.100.zip`).
3. Extract and open `redis-server.exe` to start the server.
4. Open a new terminal and run `redis-cli.exe` to connect.

> ⚠️ This version is **not recommended** for production use. Use **WSL** or **Memurai** instead.

---

### ✅ Verification

After installation, you can test Redis using:

```bash
redis-cli
127.0.0.1:6379> PING
PONG
```

---
