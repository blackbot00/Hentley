from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)

from config import BOT_TOKEN
from handlers import start
from handlers import registration
from handlers import dashboard
from handlers import ai_chat

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start.start))
app.add_handler(registration.conv_handler)
app.add_handler(CallbackQueryHandler(dashboard.dashboard_router))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_chat.ai_chat))

print("🤍 Couple Dating Bot Running...")
app.run_polling()
