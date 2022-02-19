from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *


updater = Updater('5189995160:AAGk0PWWpC055gY1bQ3Pl74OvGGOlMhWptc')

updater.dispatcher.add_handler(CommandHandler('hello', hi_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('date', date_command))
updater.dispatcher.add_handler(CommandHandler('calculate', calculate_command))

print('server start')
updater.start_polling()
updater.idle()
