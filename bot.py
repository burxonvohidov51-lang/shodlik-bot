import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

ADMIN_ID = 1487812692


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    await update.message.reply_text(
        "✅ Бот работает\n\n"
        "/products\n"
        "/orders\n"
        "/expenses"
    )


async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📦 PRODUCTS OK")


async def orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 ORDERS OK")


async def expenses(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 EXPENSES OK")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("products", products))
app.add_handler(CommandHandler("orders", orders))
app.add_handler(CommandHandler("expenses", expenses))

app.run_polling()
