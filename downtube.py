from pytube import YouTube
from telegram import Update
from telegram.ext import CallbackContext

from os import chdir, getcwd, listdir, remove, mkdir
from os.path import isfile, abspath, exists
import json
import shutil
import re

ai_mds = "CAACAgEAAxkBAAMaYUNaxDH88o_HIzxCLwhe9FnO6-8AAtoAA8sd-Udi2aFiYcSXgyAE"

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
#emoji_pattern.sub(r'', text) # no emoji

def audio(update: Update, context: CallbackContext) -> None:
    resposta1 = update.message.reply_text("Peraê.")

    try:
        yt = YouTube(context.args[0])

        pasta = emoji_pattern.sub(r'', yt.title)
        pasta = pasta.replace("|","")
        titulo = f"{pasta}.mp4"

        retorno = yt.title

        baixar = yt.streams.filter(mime_type="audio/mp4")[-1]
        tamanho = round((baixar.filesize)/(1024*1024),2)

        retorno += f"\nTamanho ~ {tamanho}Mb"

        if tamanho > 30:
            retorno += "Arquivo maior que 30MB"
            update.message.reply_sticker(ai_mds)

        resposta1.edit_text(retorno)

        if tamanho < 30:
            if not exists(pasta):
                mkdir(pasta)

            chdir(pasta)

            baixar.download(filename=titulo)

            if isfile(titulo):
                update.message.reply_audio(audio=open(abspath(titulo),'rb'))

            chdir("../")

            shutil.rmtree(abspath(pasta))
    except:
        resposta1.edit_text("Não consigo.")
        update.message.reply_sticker(ai_mds)

def video(update: Update, context: CallbackContext) -> None:
    resposta1 = update.message.reply_text("Peraê.")
    try:
        yt = YouTube(context.args[0])

        pasta = emoji_pattern.sub(r'', yt.title)
        pasta = pasta.replace("|","")
        titulo = f"{pasta}.mp4"

        retorno = yt.title

        baixar = yt.streams.get_highest_resolution()
        tamanho = round((baixar.filesize)/(1024*1024),2)

        retorno += f"\nTamanho ~ {tamanho}Mb\n"

        if tamanho > 30:
            retorno += "Arquivo maior que 30MB"
            update.message.reply_sticker(ai_mds)
            

        resposta1.edit_text(retorno)

        if tamanho < 30:
            if not exists(pasta):
                mkdir(pasta)

            chdir(pasta)

            baixar.download(filename=titulo)

            if isfile(titulo):
                update.message.reply_video(video=open(abspath(titulo),'rb'))

            chdir("../")

            shutil.rmtree(abspath(pasta))
    except:
        resposta1.edit_text("Não consigo.")
        update.message.reply_sticker(ai_mds)
