import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY")

if not TELEGRAM_BOT_TOKEN or not API_FOOTBALL_KEY:
    raise ValueError("⚠️ Debes configurar TELEGRAM_BOT_TOKEN y API_FOOTBALL_KEY en las variables de entorno.")
