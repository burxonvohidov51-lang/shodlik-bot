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

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    await update.message.reply_text(
        "/products - товары\n"
        "/orders - заказы\n"
        "/expenses - расходы"
    )

# PRODUCTS
async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    try:
        url = f"https://api-seller.uzum.uz/api/seller-openapi/v1/product/shop/{SHOP_ID}"
r = requests.get(url, headers=headers)
data = r.json()

await update.message.reply_text(
    f"Status: {r.status_code}\n\n{str(data)[:3000]}"
)
return

text = "📦 Товары:\n\n""

        for item in data[:20]:
            text += f"{item.get('title','Без названия')}\n"
            text += f"SKU: {item.get('skuId')}\n\n"

        await update.message.reply_text(text)

    except Exception as e:
        await update.message.reply_text(f"Ошибка:\n{e}")

# ORDERS
async def orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    try:
        url = "https://api-seller.uzum.uz/api/seller-openapi/v1/finance/orders"

        r = requests.get(url, headers=headers)

        await update.message.reply_text(
            f"Статус: {r.status_code}"
        )

    except Exception as e:
        await update.message.reply_text(str(e))

# EXPENSES
async def expenses(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    try:
        url = "https://api-seller.uzum.uz/api/seller-openapi/v1/finance/expenses"

        r = requests.get(url, headers=headers)

        await update.message.reply_text(
            f"Статус: {r.status_code}"
        )

    except Exception as e:
        await update.message.reply_text(str(e))

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("products", products))
app.add_handler(CommandHandler("orders", orders))
app.add_handler(CommandHandler("expenses", expenses))

app.run_polling()
