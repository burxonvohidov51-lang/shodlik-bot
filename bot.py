from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8928390346:AAEVKjM8VLX0_B9tSgP0KKhAxeYp2Ndj4tY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ассалому алайкум! Shodlik Bot ишга тушди.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
