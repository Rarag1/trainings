from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apps import *
from Game import *

app = ApplicationBuilder().token("5886826050:AAE05-_E_5k8mkGOC1SnFudRMkBVkEhsOwg").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("game", game))

print('Server start')
app.run_polling()