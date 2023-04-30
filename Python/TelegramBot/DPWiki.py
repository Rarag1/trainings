from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import requests

DPWiki_URL = "https://7011.deeppavlov.ai/model"


async def DPWiki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}. Вас приветствует DeepPavlov, библиотека для поиска ответов в Википедии.')
    await update.message.reply_text(f'Введите /wiki ваш запрос, чтобы начать.')


async def wiki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = " ".join(update.message.text.split()[1:])
    print(msg)
    try:
        res = requests.post(
            DPWiki_URL, json={'question_raw': [msg]}, verify=None).json()
        print(res)
        await update.message.reply_text(res)
    except:
        await update.message.reply_text("Не нашлось ответа.")
