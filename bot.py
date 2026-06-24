import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")
UZUM_API = os.getenv("UZUM_API_KEY")

ADMIN_ID = 1487812692
SHOP_ID = 75362

headers = {
    "Authorization": UZUM_API,
    "Content-Type": "application/json"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    await update.message.reply_text(
        "/products - товары\n"
        "/price sku цена\n"
        "/orders\n"
        "/expenses"
    )

async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    await update.message.reply_text("Список товаров загружается...")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("products", products))

app.run_polling()
