from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database.db import get_user, update_balance

async def wallet(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = get_user(query.from_user.id)

    keyboard = [
        [InlineKeyboardButton("➕ Depositar $50", callback_data="deposit")],
        [InlineKeyboardButton("➖ Retirar $50", callback_data="withdraw")],
        [InlineKeyboardButton("⬅️ Volver", callback_data="back_main")]
    ]
    await query.edit_message_text(
        f"💼 Tu saldo actual: ${user.balance:.2f}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def wallet_action(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data == "deposit":
        update_balance(query.from_user.id, 50)
        text = "Has depositado $50 💵"
    elif query.data == "withdraw":
        update_balance(query.from_user.id, -50)
        text = "Has retirado $50 💸"
    await query.answer(text, show_alert=True)
    await wallet(update, context)
