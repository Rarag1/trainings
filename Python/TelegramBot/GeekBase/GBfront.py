from telegram import Update
from telegram.ext import *
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import numpy as np
import pandas as pd
from GeekBase.GBback import wright1, find1, delete1

reply_keyboard = [['/geekbase', '/wright'],
                  ['/find', '/delete']]
markup1 = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

async def geekbase(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}. Чего изволите?', reply_markup=markup1)
    await update.message.reply_text(f'/geekbase - введите имя файла.')
    msg = update.message.text.split()
    print(msg)
    global file
    file = msg[1]
    print(file)
    await update.message.reply_text(f'/wright, /find, /delete - выберите действие.')

async def wright(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/wright - введите ФИО, телефон, коментарий.")
    msg = update.message.text.split()
    print(msg)
    d_wright = ",".join([msg[1],msg[2],msg[3]])
    print(d_wright)
    global file
    wrighted = wright1(file, d_wright)
    print(wrighted)
    await update.message.reply_text(f"Получилось\n{wrighted}")

async def find(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/find - введите поле поиска и значение поля.")
    msg = update.message.text.split()
    print(msg)
    global file
    global find_field
    global find_value
    find_field = msg[1]
    find_value = msg[2]
    global finded
    finded = find1(file, find_field, find_value)
    print(finded)
    await update.message.reply_text(f"Искомое значение\n{finded}")
    

async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/delete - удалить ранее найденное значение (y,n)?")
    msg = update.message.text.split()
    print(msg)
    global file
    d_delete = msg[1]
    if d_delete == 'y': 
        file = delete1(file, find_field, find_value)
    print(file)
    await update.message.reply_text(f"Получилось\n{file}")
    