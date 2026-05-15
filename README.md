# PyCon 2026 Labs

Welcome! This repo contains a collection of hands-on labs built for PyCon 2026. Each lab is self-contained and designed to run entirely inside a **GitHub Codespace** — no local setup required. Just open the Codespace, pick a lab, and start building!

---

## Getting Started

These labs are built to run in a **GitHub Codespace**. All dependencies, extensions, and environment configuration are pre-installed. To get started:

1. Click **Code** > **Codespaces** > **Create codespace on main** from the GitHub repo page.
2. Wait for the Codespace to finish setting up.
3. Pick a lab below and follow its `README.md`.

---

## Labs

### AI Travel Agent with Azure DocumentDB

**Folder:** `lab-documentdb/`

Build and interact with an AI travel agent that uses **Azure DocumentDB** for vector search, document storage, and conversation history. Explore how the agent retrieves cruise destinations using semantic similarity and persists booking data — all through a live FastAPI backend.

**Technologies:**
- Python / FastAPI
- Azure DocumentDB (vector search, document collections)
- Azure OpenAI
- VS Code Azure Extension

---

### GitHub Copilot CLI

**Folder:** `lab-ghcp-cli/`

You've inherited a broken Python quiz game. Use **GitHub Copilot CLI** to document functions, plan and generate a pytest test suite, and track down the bug — all from an interactive terminal session with GitHub Copilot.

**Technologies:**
- Python / pytest
- GitHub Copilot CLI
- Natural language prompting and plan mode

---

### Semantic Note Search with Azure PostgreSQL

**Folder:** `lab-postgressql/`

Build and interact with a semantic search app that uses Azure PostgreSQL for vector search, structured note storage, and semantic retrieval. Explore how the app finds notes by meaning instead of exact keywords by generating embeddings with Microsoft Foundry and retrieving similar notes from a PostgreSQL database.

**Technologies:**
- Python
- Azure Database for PostgreSQL Flexible Server
- pgvector (vector similarity search)
- Microsoft Foundry
- Embedding moel (text-embedding-3-small)

---

## Resetting a Lab

Each lab has a `reset.sh` script that restores it to its starting state. To reset all labs at once:

```bash
bash reset-all.sh
```

## For Administrators

**Important:** Before running these labs with participants, complete all setup instructions available in the **ADMIN.md** files for `lab-documentdb` and `lab-postgressql`. This includes provisioning Azure resources, configuring authentication, and verifying connectivity for all required services.

---