from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import numpy as np
from random import randint

global rang
global lucky
global A
A = np.zeros((4, 4))

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}. Сиграем в крестики-нолики?')
    await update.message.reply_text(f'{A}')
    await update.message.reply_text(f'Введите /begin, чтобы начать.')
   

async def begin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Введите /move и 2-е координаты (от 0 до 3) хода через пробел.')
    global rang
    rang = randint(1, 2)
    if rang == 1:
        await update.message.reply_text(f"Ходит 1-й игрок.")
    else:
        await update.message.reply_text(f"Ходит 2-ой игрок.")

async def move(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global A
    global rang
    while True:
        if A[0, :].sum() == 4 or A[1, :].sum() == 4 or A[2, :].sum() == 4 or A[3, :].sum() == 4 or\
            A[:, 0].sum() == 4 or A[:, 1].sum() == 4 or A[:, 2].sum() == 4 or A[:, 3].sum() == 4 or\
                np.diag(A).sum() == 4 or np.diag(-A).sum() == 4:
            await update.message.reply_text(f"Выиграл 1-й игрок.")
            break
        elif A[0, :].sum() == 20 or A[1, :].sum() == 20 or A[2, :].sum() == 20 or A[3, :].sum() == 20 or\
            A[:, 0].sum() == 20 or A[:, 1].sum() == 20 or A[:, 2].sum() == 20 or A[:, 3].sum() == 20 or\
                np.diag(A).sum() == 20 or np.diag(-A).sum() == 20:
            await update.message.reply_text(f"Выиграл 2-ой игрок.")
            break

        lucky = randint(0, 1) # есть возможность перебивать занятую позицию, если удача с тобой
        if rang == 1:            
            msg = update.message.text
            print(msg)
            coords = msg.split()
            i = int(coords[1])
            j = int(coords[2])
            if A[i, j] == 0:
                A[i, j] = 1
            elif A[i, j] != 0 and lucky != 0:
                A[i, j] = 1
            await update.message.reply_text(f'{A}')
            await update.message.reply_text(f'lucky ={lucky}')
            rang += 1
            await update.message.reply_text(f"Ходит 2-ой игрок.")
            break
        else:            
            msg = update.message.text
            print(msg)
            coords = msg.split()
            i = int(coords[1])
            j = int(coords[2])
            if A[i, j] == 0:
                A[i, j] = 5
            elif A[i, j] != 0 and lucky != 0:
                A[i, j] = 5
            await update.message.reply_text(f'{A}')
            await update.message.reply_text(f'lucky ={lucky}')
            rang -= 1
            await update.message.reply_text(f"Ходит 1-ый игрок.")
            break
        print(type(A))
        # rang = randint(1, 2)  # добавлен фактор рандомного призового хода
        # if rang == 1:
        #     await update.message.reply_text(f"Ходит 1-й игрок.")
        # else:
        #     await update.message.reply_text(f"Ходит 2-ой игрок.")