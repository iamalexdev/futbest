from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from handlers.start import start
from handlers.wallet import wallet, wallet_action
from handlers.bets import bets
from database.db import init_db
from config import TELEGRAM_BOT_TOKEN

async def router(update, context):
    query = update.callback_query
    data = query.data
    if data == "wallet":
        await wallet(update, context)
    elif data in ["deposit", "withdraw"]:
        await wallet_action(update, context)
    elif data == "bets":
        await bets(update, context)
    elif data == "back_main":
        await start(update, context)

if __name__ == "__main__":
    init_db()
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(router))
    print("🤖 FutBetMaster está en línea...")
    app.run_polling()
