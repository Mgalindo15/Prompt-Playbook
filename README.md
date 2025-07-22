# 🧠 Prompt-Playbook

A library of prompt patterns for conversational LLMs that help people **decide, learn, and act**.  
Includes games, planners, tutors, and task decomposers—each with annotated techniques and runnable CLI demos.

---

## ✨ Active Patterns

| Prompt-Series | Use-case | Files | **Similar Tech** |
|---------|----------|-------|------------------|
| Snapshot! Games | Auto-Generate Code Comprehension Mini-Games | [patterns/snapshot_games.md](patterns/snapshot_games.md) | Zybooks, LeetCode “Playground” |

...

---


## 🚀 CLI Quickstart

### 🔧 Setup

```bash
# 1. Clone & enter
git clone https://github.com/Mgalindo15/prompt-playbook
cd prompt-playbook

# 2. Install
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3. Add your .env file (see `.env.example`)
```

### Snapshot Game

```bash
python scripts/play_snapshot.py \
  --variant blank \
  --language "SQL" \
  --features "JOINs"
  ```
