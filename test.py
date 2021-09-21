from telegram import Update
from telegram.ext import CallbackContext
import sqlite3

from random import choice
from os import chdir, getcwd, listdir, remove
from os.path import isfile,abspath
import json
import shutil
import instaloader

ai_mds = "CAACAgEAAxkBAAMaYUNaxDH88o_HIzxCLwhe9FnO6-8AAtoAA8sd-Udi2aFiYcSXgyAE"

haha = "CAACAgEAAxkBAANHYUNw3BtpUtR0gD1bsTaFr3hExi8AAkgBAAI--LFHYNQOiaTBkfogBA"

idYsrael = 580196408

def test(update: Update, context: CallbackContext) -> None:
#     pass

# def teste():
    hast = (context.args[0]).replace("#",'')
    
    app = instaloader.Instaloader()
    hasht = instaloader.Hashtag.from_name(app.context,hast)
    pasta = f"#{hasht.name}-13"
    for post in hasht.get_top_posts():
        app.download_post(post,target=pasta)

    chdir(pasta)
    sorteio = []

    for file in listdir():
        
        if isfile(file):
            
            if file.endswith(".jpg"):
                sorteio.append(file)

    
    arquivo = abspath(choice(sorteio))
    print(arquivo)
    update.message.reply_photo(photo=open(arquivo,"rb"))

    chdir("../")
    shutil.rmtree(abspath(pasta))

# teste()