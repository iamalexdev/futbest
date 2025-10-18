from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database.db import get_user, create_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)
    if not user:
        create_user(update.effective_user.id, update.effective_user.username)
        text = "👋 Bienvenido a FutBetMaster! Tu cuenta ha sido creada con $100 de saldo inicial."
    else:
        text = f"👋 Bienvenido de nuevo, {update.effective_user.first_name}!"

    keyboard = [
        [InlineKeyboardButton("💰 Mi Billetera", callback_data="wallet")],
        [InlineKeyboardButton("⚽ Apuestas en Vivo", callback_data="bets")]
    ]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
