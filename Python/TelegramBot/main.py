from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import config
# from apps import *
from Game import *
from GeekBase.GBfront import *

app = ApplicationBuilder().token(config.TOKEN).build()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}', reply_markup=markup0)

reply_keyboard = [['/game'], ['/geekbase'], ['/calc']]
markup0 = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("game", game))
app.add_handler(CommandHandler("begin", begin))
app.add_handler(CommandHandler("move", move))
# app.add_handler(MessageHandler("filter.TEXT", move))

app.add_handler(CommandHandler("geekbase", geekbase))
app.add_handler(CommandHandler("wright", wright))
app.add_handler(CommandHandler("find", find))
app.add_handler(CommandHandler("delete", delete))

print('Server start')
app.run_polling()