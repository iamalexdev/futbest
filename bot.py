from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from database.db import init_db, get_user, create_user
from handlers.wallet import wallet_menu
from handlers.bets import bets_menu

TOKEN = "7630853977:AAGrnl9XdzC-8eONDIp-8NM-uqimlYboFcc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)
    if not user:
        create_user(update.effective_user.id, update.effective_user.username)
        await update.message.reply_text("👋 ¡Bienvenido! Tu cuenta ha sido creada.")
    else:
        await update.message.reply_text(f"¡Hola {user.username}! 👋")

    keyboard = [
        [InlineKeyboardButton("💰 Mi Billetera", callback_data="wallet")],
        [InlineKeyboardButton("⚽ Apuestas", callback_data="bets")]
    ]
    await update.message.reply_text("Selecciona una opción:", 
                                    reply_markup=InlineKeyboardMarkup(keyboard))

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "wallet":
        await wallet_menu(update, context)
    elif query.data == "bets":
        await bets_menu(update, context)

if __name__ == "__main__":
    init_db()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler))
    app.run_polling()

