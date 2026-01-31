from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💖 Start Registration", callback_data="register")]
    ])

def dashboard_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 Human to Human Chat", callback_data="human")],
        [InlineKeyboardButton("🤖 Human to AI Chat", callback_data="ai")],
        [InlineKeyboardButton("✏️ Edit Profile", callback_data="edit")]
    ])
