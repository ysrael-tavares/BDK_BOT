from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters
from roll import roll,ini
from main_menu import start
from help import help
from test import test
from instagram import perfilInsta,buscaInsta
from downtube import audio, video
from conf.settings import TELEGRAM_TOKEN

updater = Updater(TELEGRAM_TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('r', roll))
updater.dispatcher.add_handler(CommandHandler('test', test))
updater.dispatcher.add_handler(CommandHandler('insta', perfilInsta))
updater.dispatcher.add_handler(CommandHandler('buscaig', buscaInsta))
updater.dispatcher.add_handler(CommandHandler('audio', audio))
updater.dispatcher.add_handler(CommandHandler('video', video))
updater.dispatcher.add_handler(CommandHandler('i', ini))

updater.start_polling()
print("Bot Iniciado")
updater.idle()