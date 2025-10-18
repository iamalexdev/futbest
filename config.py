import os

TELEGRAM_BOT_TOKEN = os.getenv("7630853977:AAGrnl9XdzC-8eONDIp-8NM-uqimlYboFcc)
API_FOOTBALL_KEY = os.getenv("aa0d5dc769cfaf7d2ad217ef96db276e")

if not TELEGRAM_BOT_TOKEN or not API_FOOTBALL_KEY:
    raise ValueError("⚠️ Debes configurar TELEGRAM_BOT_TOKEN y API_FOOTBALL_KEY en las variables de entorno.")

