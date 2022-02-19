from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime
from logger import *

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi, {update.effective_user.first_name}! Для просмотра доступных команд введите: /help')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/help\n/time\n/date\n/calculate\n')

def time_command(update: Update, context: CallbackContext):
    log(update, context)
    now_t = datetime.now().time()
    correct_time = now_t.strftime('%H:%M:%S')
    update.message.reply_text(f'Время: {correct_time}')

def date_command(update: Update, context: CallbackContext):
    log(update, context)
    now_d = datetime.now().date()
    correct_date = now_d.strftime('%d/%m/%Y')
    update.message.reply_text(f'Дата: {correct_date}')

def calculate_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    res = msg.split()
    x = int(res[1])
    oper = str(res[2])
    y = int(res[3])
    if oper == '+':
        update.message.reply_text(f'Сумма: {x + y}')
    if oper == '-': 
        update.message.reply_text(f'Разность: {x - y}')
    if oper == '*': 
        update.message.reply_text(f'Произведение: {x * y}')
    if oper == '/': 
        update.message.reply_text(f'Частное: {x / y}')

