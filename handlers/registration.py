from telegram.ext import (
    ConversationHandler, CallbackQueryHandler,
    MessageHandler, filters
)
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from utils.states import NAME, GENDER, LOOKING, AGE, BIO
from database.mongodb import users

async def start_reg(update: Update, context):
    await update.callback_query.message.reply_text(
        "💫 Let's begin…\n\nWhat should we call you?"
    )
    return NAME

async def name(update: Update, context):
    context.user_data["name"] = update.message.text
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("👨 Male", callback_data="Male"),
         InlineKeyboardButton("👩 Female", callback_data="Female"),
         InlineKeyboardButton("🌈 Other", callback_data="Other")]
    ])
    await update.message.reply_text("Select your gender 👇", reply_markup=kb)
    return GENDER

async def gender(update: Update, context):
    context.user_data["gender"] = update.callback_query.data
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("👨 Male", callback_data="Male"),
         InlineKeyboardButton("👩 Female", callback_data="Female"),
         InlineKeyboardButton("🌍 Anyone", callback_data="Anyone")]
    ])
    await update.callback_query.message.reply_text(
        "Who are you looking to connect with? 💕",
        reply_markup=kb
    )
    return LOOKING

async def looking(update: Update, context):
    context.user_data["looking"] = update.callback_query.data
    await update.callback_query.message.reply_text("How old are you? 🎂")
    return AGE

async def age(update: Update, context):
    age = int(update.message.text)
    if age < 18:
        await update.message.reply_text("⚠️ 18+ only")
        return AGE
    context.user_data["age"] = age
    await update.message.reply_text(
        "Write a short bio 💭\n\n✨ Tip: Nice bio = more replies 😉"
    )
    return BIO

async def bio(update: Update, context):
    context.user_data["bio"] = update.message.text
    users.insert_one({
        "user_id": update.effective_user.id,
        **context.user_data
    })
    await update.message.reply_text(
        "✨ *Profile Ready!*\n\nWelcome ❤️",
        parse_mode="Markdown"
    )
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(start_reg, pattern="register")],
    states={
        NAME: [MessageHandler(filters.TEXT, name)],
        GENDER: [CallbackQueryHandler(gender)],
        LOOKING: [CallbackQueryHandler(looking)],
        AGE: [MessageHandler(filters.TEXT, age)],
        BIO: [MessageHandler(filters.TEXT, bio)],
    },
    fallbacks=[]
  )
