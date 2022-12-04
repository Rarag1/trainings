from telegram import Update
from telegram.ext import *
import numpy as np
import pandas as pd

async def geekbase(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}. Чего изволите?')
    await update.message.reply_text(f'/input - введите имя файла.')
    msg = update.message.text.split()
    print(msg)
    file = msg[1]
    await update.message.reply_text(f'/wright, /find, /delete - выберите действие.')

async def wright(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/wright - введите ФИО, телефон, коментарий.")
    msg = update.message.text.split()
    print(msg)
    fio = msg[1], tel =  msg[2], com =  msg[3]

async def find(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/find - введите поле поиска и значение поля.")
    msg = update.message.text.split()
    print(msg)
    find_field = msg[1], find_value =  msg[2]

async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/delete - введите поле поиска и значение поля.")
    msg = update.message.text.split()
    print(msg)
    find_field = msg[1], find_value =  msg[2]
    await update.message.reply_text(f"/delete - подтвердите удаление.")