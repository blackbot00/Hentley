from telegram import Update
from telegram.ext import ContextTypes
from utils.keyboards import dashboard_kb

async def dashboard_router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "human":
        await query.message.reply_text(
            "💬 Human to Human Chat\n\nFinding real connections 💕"
        )

    elif query.data == "ai":
        await query.message.reply_text(
            "🤖 AI Companion\n\nTalk freely. I'm here 🤍"
        )

    elif query.data == "edit":
        await query.message.reply_text(
            "✏️ Edit Profile\n\nChoose what to update ✨"
      )
