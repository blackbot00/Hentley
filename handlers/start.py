from telegram import Update
from telegram.ext import ContextTypes
from utils.keyboards import start_kb

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ *Welcome to ❤️ CoupleSphere*\n\n"
        "Find real connections.\n"
        "Or chat with our smart AI 🤍\n\n"
        "🔒 Safe • 💬 Private • ⭐ Premium",
        reply_markup=start_kb(),
        parse_mode="Markdown"
    )
