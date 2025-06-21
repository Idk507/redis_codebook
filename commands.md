Here’s a comprehensive list of **Redis commands** organized by category — ideal for beginners to advanced usage.

---

## 📌 1. **Basic Commands**

| Command           | Description                       |
| ----------------- | --------------------------------- |
| `SET key value`   | Set a key to a value              |
| `GET key`         | Get the value of a key            |
| `DEL key`         | Delete a key                      |
| `EXISTS key`      | Check if a key exists             |
| `EXPIRE key secs` | Set TTL (Time-To-Live) in seconds |
| `TTL key`         | Get remaining TTL for a key       |
| `KEYS pattern`    | List keys by pattern (e.g., `*`)  |
| `FLUSHALL`        | Delete **all** keys in all DBs    |

---

## 🔗 2. **String Commands**

```bash
SET mykey "Hello"
GET mykey
APPEND mykey " World"
STRLEN mykey
INCR counter     # Auto-increments integer
DECR counter
```

---

## 📑 3. **Hash (Dictionary-like)**

```bash
HSET user:1 name "Alice" age "30"
HGET user:1 name
HGETALL user:1
HDEL user:1 age
HEXISTS user:1 name
HINCRBY user:1 age 1
```

---

## 📋 4. **List Commands (Linked list)**

```bash
LPUSH mylist "a" "b" "c"  # c is head
RPUSH mylist "x" "y"
LPOP mylist               # remove from left
RPOP mylist               # remove from right
LRANGE mylist 0 -1        # get all elements
LLEN mylist               # length of list
```

---

## 🔢 5. **Set Commands (Unordered unique values)**

```bash
SADD myset "apple" "banana"
SREM myset "banana"
SMEMBERS myset
SISMEMBER myset "apple"
SUNION set1 set2
SINTER set1 set2
```

---

## 🎯 6. **Sorted Set (Ordered by score)**

```bash
ZADD scores 100 "Alice" 200 "Bob"
ZRANGE scores 0 -1 WITHSCORES
ZREVRANGE scores 0 -1
ZINCRBY scores 10 "Alice"
ZREM scores "Bob"
ZRANK scores "Alice"
```

---

## 📣 7. **Pub/Sub Messaging**

```bash
SUBSCRIBE news
PUBLISH news "Redis 7 released!"
```

In two terminals:

* Terminal A: `redis-cli` → `SUBSCRIBE news`
* Terminal B: `redis-cli` → `PUBLISH news "Hello"`

---

## 💾 8. **Persistence & Server Info**

| Command        | Description                |
| -------------- | -------------------------- |
| `SAVE`         | Snapshot the DB now        |
| `BGSAVE`       | Save DB in background      |
| `INFO`         | View server stats/config   |
| `MONITOR`      | Watch real-time commands   |
| `CONFIG GET *` | View all config parameters |

---

## 🧪 9. **Transactions & Scripting**

```bash
MULTI
SET key1 "Hello"
SET key2 "World"
EXEC               # Execute all at once
```

Lua scripting:

```bash
EVAL "return 2+2" 0
```

---

## 🛠️ 10. **Useful Tools**

* `redis-cli`: Command line client
* `RedisInsight`: GUI for Redis
* `MONITOR`: Debug by watching live traffic
* `SCAN`: Safer alternative to `KEYS` in production

---

### ✅ Example Session:

```bash
127.0.0.1:6379> SET lang "Redis"
OK
127.0.0.1:6379> GET lang
"Redis"
127.0.0.1:6379> DEL lang
(integer) 1
```

---

