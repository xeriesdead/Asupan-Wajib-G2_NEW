# Telegram Media Sharing Bot

## Overview

Telegram bot for media sharing with admin upload, broadcast, and scheduled broadcast features. Deployed on Railway; source managed on GitHub. Replit is used as a code editor only.

## Stack

- **Language**: Python 3
- **Framework**: FastAPI + uvicorn (webhook mode)
- **Bot library**: python-telegram-bot 20.7
- **Database**: SQLite (with WAL mode, connection pool)
- **Deployment**: Railway (uses `RAILWAY_PUBLIC_DOMAIN` for webhook URL)

## Key Files

- `main.py` — bot logic, FastAPI app, all handlers
- `config.py` — configuration loaded from environment variables
- `requirements.txt` — Python dependencies
- `Procfile` — Railway process definition

## Required Environment Variables

| Variable | Description |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Bot token from @BotFather (required) |
| `CHANNEL` | Channel username e.g. `@YourChannel` |
| `CHANNEL_ID` | Channel numeric ID |
| `BOT_USERNAME` | Bot username without `@` |
| `ADMIN_IDS` | Comma-separated admin Telegram user IDs |
| `BACKUP_CHAT_ID` | Chat ID to receive DB backups |
| `WEBHOOK_DOMAIN` | Override webhook URL (optional) |

## Running (Railway)

Deployed automatically via GitHub push. Railway sets `RAILWAY_PUBLIC_DOMAIN` which the bot uses to register its webhook.

## User Preferences

- This project runs on Railway + GitHub. Replit is used as a code editor only — do not set up a run workflow or attempt to run the bot here.
