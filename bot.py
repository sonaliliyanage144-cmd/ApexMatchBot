from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler
)

import random
import asyncio

TELEGRAM_TOKEN = "8898791061:AAHZUoQdWsuCv4Zsv-S4a06fgk6XtEaE6T4" 

# START
async def start(update, context):

    keyboard = [
        [InlineKeyboardButton("📈 Get Rise/Fall Signal", callback_data="signal")],
        [InlineKeyboardButton("🔒 VIP", callback_data="vip")],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
🔥 APEX RISE/FALL BOT 🔥

✅ Volatility Signals
✅ Fast Analysis
✅ Rise/Fall Trading

Choose option below 👇
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )

# BUTTONS
async def button(update, context):

    query = update.callback_query
    await query.answer()

    if query.data == "signal":

        msg = await query.message.reply_text(
            "🔍 Analyzing Market..."
        )

        await asyncio.sleep(2)

        await msg.edit_text(
            "📊 Checking Trend..."
        )

        await asyncio.sleep(2)

        markets = [
            "Volatility 10",
            "Volatility 25",
            "Volatility 50",
            "Volatility 75",
            "Volatility 100"
        ]

        signal = random.choice([
            "📈 RISE",
            "📉 FALL"
        ])

        duration = random.choice([
            "1 Minute",
            "3 Minutes",
            "5 Minutes",
            "10 Minutes"
        ])

        market = random.choice(markets)

        final = f'''
🔥 SIGNAL READY 🔥

💹 Market: {market}

📊 Trade: {signal}

⏰ Duration: {duration}

🎯 Accuracy: 92%

⚠️ Manage Your Risk Properly
'''

        await msg.edit_text(final)

    elif query.data == "vip":

        await query.message.reply_text(
            "🔒 VIP SYSTEM COMING SOON!"
        )

    elif query.data == "help":

        await query.message.reply_text(
            "📌 Click Get Signal to receive Rise/Fall signals."
        )

# APP
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("🔥 Rise/Fall Bot Running 🔥")

app.run_polling()
