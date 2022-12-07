from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}', reply_markup=markup2)
    await update.message.reply_text(f'| + | - | * | / |  - выберите действие.')
    await update.message.reply_text(f"/calc - введите что хотите посчитать черз пробел.")
    await update.message.reply_text(f"Example: /calc 3 + 7")
    msg = update.message.text.split()
    print(msg)
    global a
    global b
    global action
    global result
    a = int(msg[1])
    b = int(msg[3])
    action = msg[2]
    if action == "+":
        add(a,b)
    elif action == "-":
        sub(a,b)
    elif action == "*":
        mult(a,b)
    elif action == "/":
        div(a,b)
    await update.message.reply_text(f'{a} {action} {b} = {result}')
    print(f'{a} {action} {b} = {result}')

def add(a,b):
    global result
    result = a + b
    return result

def sub(a,b):
    global result
    result = a - b
    return result

def mult(a,b):
    global result
    result = a * b
    return result

def div(a,b):
    global result
    result = a / b
    return result



reply_keyboard = [['/add', '/sub'],
                 ['/mult', '/div']]
markup2 = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

# async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     result = a + b
#     await update.message.reply_text(f'{a}{action}{b} = {result} ')
#     print(result)

# async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     result = a - b
#     await update.message.reply_text(f'{a}{action}{b} = {result} ')
#     print(result)

# async def mult(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     result = a * b
#     await update.message.reply_text(f'{a}{action}{b} = {result} ')
#     print(result)

# async def div(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     result = a / b
#     await update.message.reply_text(f'{a}{action}{b} = {result} ')
#     print(result)