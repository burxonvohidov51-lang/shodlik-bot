from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "ТВОЙ_ТОКЕН_ОТ_BOTFATHER"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ассалому алайкум! Shodlik Bot ишга тушди.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
