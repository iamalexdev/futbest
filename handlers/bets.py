import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import API_FOOTBALL_KEY
from database.db import get_user, update_balance

API_URL = "https://v3.football.api-sports.io/fixtures?live=all"
HEADERS = {"x-apisports-key": API_FOOTBALL_KEY}

async def bets(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.edit_message_text("Cargando partidos en vivo... ⚽")

    try:
        res = requests.get(API_URL, headers=HEADERS)
        matches = res.json().get("response", [])
    except Exception:
        matches = []

    if not matches:
        await query.edit_message_text("😔 No hay partidos en vivo ahora mismo.")
        return

    buttons = []
    for m in matches[:5]:
        home = m["teams"]["home"]["name"]
        away = m["teams"]["away"]["name"]
        fixture_id = m["fixture"]["id"]
        buttons.append([InlineKeyboardButton(f"{home} vs {away}", callback_data=f"bet_{fixture_id}")])

    await query.edit_message_text("Selecciona un partido para apostar:", reply_markup=InlineKeyboardMarkup(buttons))
