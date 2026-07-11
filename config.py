# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL", "@Asupan_Wajib")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1003512802994"))
BOT_USERNAME = os.getenv("BOT_USERNAME", "Asupan_Wajib_Bot")
ADMIN_IDS = [int(x.strip()) for x in os.getenv("ADMIN_IDS", "8441460682").split(",")]
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))

# URL publik tempat bot di-deploy (Railway otomatis isi RAILWAY_PUBLIC_DOMAIN)
# Contoh: https://mybot.up.railway.app
_railway_domain = os.getenv("RAILWAY_PUBLIC_DOMAIN", "")
_replit_domain = os.getenv("REPLIT_DOMAINS", "").split(",")[0].strip()
_manual_domain = os.getenv("WEBHOOK_DOMAIN", "")

if _manual_domain:
    WEBHOOK_URL = _manual_domain.rstrip("/")
elif _railway_domain:
    WEBHOOK_URL = f"https://{_railway_domain}"
elif _replit_domain:
    WEBHOOK_URL = f"https://{_replit_domain}"
else:
    WEBHOOK_URL = "https://yourdomain.com"

WEBHOOK_PATH = "/webhook/telegram"

DATABASE_PATH = os.getenv("DATABASE_PATH", "database.db")
BACKUP_CHAT_ID = int(os.getenv("BACKUP_CHAT_ID", "8441460682"))
AUTO_DELETE_TIMEOUT = int(os.getenv("AUTO_DELETE_TIMEOUT", "3600"))  # 1 jam
BATCH_TIMEOUT = 10
BACKUP_INTERVAL = 21600  # 6 jam
BACKUP_DIR = "backups"
MAX_BACKUPS = 10

if not TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN not set in .env!")
