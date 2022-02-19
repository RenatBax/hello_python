from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def log(update: Update, context: CallbackContext):
    file = open('logFbot.cvs', 'a', encoding= 'UTF-8')
    file.write(f'{update.effective_user.first_name} / {update.effective_user.id} / {update.message.text} / {update.message.contact} / {update.message.reply_text}\n')
    file.close()