from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes
import config
from apps import *
from Game import *

app = ApplicationBuilder().token(config.TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("game", game))
app.add_handler(CommandHandler("begin", begin))
app.add_handler(CommandHandler("move", move))
# app.add_handler(MessageHandler("filter.TEXT", move))

print('Server start')
app.run_polling()
