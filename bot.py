import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")
UZUM_API = os.getenv("UZUM_API_KEY")

ADMIN_ID = 1487812692
SHOP_ID = 75362


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Shodlik Bot\n\n"
        "/products"
    )


async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = f"https://api-seller.uzum.uz/api/seller-openapi/v1/product/shop/{SHOP_ID}?sortBy=DEFAULT&order=ASC&size=20&page=0&filter=ALL"

        headers = {
            "Authorization": UZUM_API
        }

        r = requests.get(url, headers=headers)

        if r.status_code != 200:
            await update.message.reply_text(
                f"Ошибка {r.status_code}\n\n{r.text}"
            )
            return

        data = r.json()

        text = "📦 Товары:\n\n"

        for product in data.get("productList", [])[:10]:
            title = product.get("title", "Без названия")
            price = product.get("price", "Нет цены")
            quantity = product.get("quantityAvailable", 0)

            text += (
                f"🛍 {title}\n"
                f"💰 Цена: {price}\n"
                f"📦 Остаток: {quantity}\n\n"
            )

        if text == "📦 Товары:\n\n":
            text += "Товары не найдены."

        await update.message.reply_text(text)

    except Exception as e:
        await update.message.reply_text(f"Ошибка:\n{e}")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("products", products))

app.run_polling()
