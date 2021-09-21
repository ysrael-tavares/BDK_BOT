from telegram import Update
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, PrefixHandler, CallbackContext
from random import randint
from stickers import sticker

def roll(update: Update, context: CallbackContext):
    somas = (context.args[0].replace(' ','')).split('+')
    resultado = 0

    for parcela in somas:

        if parcela.find('d') > -1:
            parcela = parcela.split('d')

            for i in range(int(parcela[0])):
                resultado_dado = randint(1,int(parcela[1]))
                resultado += resultado_dado

                if resultado_dado == 20 or resultado_dado == 1:
                    update.message.reply_text("{} Natural @{}".format(resultado_dado,update.effective_user.username))
                    update.message.reply_sticker(sticker(resultado_dado))
        else:
            resultado += int(parcela)
    
    update.message.reply_text('@{}: {}'.format(update.effective_user.username,resultado))

def ini(update: Update, context: CallbackContext):
    somas = int(context.args[0])
    resultado = ""

    for parcela in range(somas):
        resultado_dado = str(randint(1,20))
        resultado += resultado_dado
        if parcela < somas-1:
            resultado += ","
    
    update.message.reply_text('@{}: {}'.format(update.effective_user.username,resultado))