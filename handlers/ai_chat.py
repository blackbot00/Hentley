from services.openrouter import ask_ai

async def ai_chat(update, context):
    reply = ask_ai(update.message.text)
    await update.message.reply_text(reply)
