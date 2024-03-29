from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import config
from DPWiki import *
from Calc import *
from Game import *
from GeekBase.GBfront import *

app = ApplicationBuilder().token(config.TOKEN).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}', reply_markup=markup0)

reply_keyboard = [['/DPWiki'], ['/game'], ['/geekbase'], ['/calc']]
markup0 = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

app.add_handler(CommandHandler("DPWiki", DPWiki))
app.add_handler(CommandHandler("wiki", wiki))

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("game", game))
app.add_handler(CommandHandler("begin", begin))
app.add_handler(CommandHandler("move", move))
# app.add_handler(MessageHandler("filter.TEXT", move))

app.add_handler(CommandHandler("geekbase", geekbase))
app.add_handler(CommandHandler("wright", wright))
app.add_handler(CommandHandler("find", find))
app.add_handler(CommandHandler("delete", delete))

app.add_handler(CommandHandler("calc", calc))
# app.add_handler(CommandHandler("add", add))
# app.add_handler(CommandHandler("sub", sub))
# app.add_handler(CommandHandler("mult", mult))
# app.add_handler(CommandHandler("div", div))

print('Server start')
app.run_polling()
