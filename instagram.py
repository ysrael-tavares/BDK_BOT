from telegram import Update
from telegram.ext import CallbackContext
import sqlite3

from os import chdir, getcwd, listdir, remove
from os.path import isfile,abspath
import json
import shutil
import instaloader

ai_mds = "CAACAgEAAxkBAAMaYUNaxDH88o_HIzxCLwhe9FnO6-8AAtoAA8sd-Udi2aFiYcSXgyAE"

haha = "CAACAgEAAxkBAANHYUNw3BtpUtR0gD1bsTaFr3hExi8AAkgBAAI--LFHYNQOiaTBkfogBA"

idYsrael = 580196408

def buscaInsta(update: Update, context: CallbackContext) -> None:
    pesquisa = context.args[0]
    resposta1 = update.message.reply_text("Peraê.")
    resposta = ""
    try:
        app = instaloader.Instaloader()
        app.login("seg_runeterra","learsy10")
        busca = instaloader.TopSearchResults(app.context,pesquisa)

        resultados = list(busca.get_profiles())
        resposta += "Perfis Encontrados:\n"
        
        for post in resultados[0:10]:
            resposta += f"- {post.username}  ({'Privado' if post.is_private else 'Aberto'}) {'✔️' if post.is_verified else ''}\n"
        
        resposta1.delete()
        update.message.reply_text(resposta)
    
    except:
        resposta1.edit_text("Não consigo.")
        update.message.reply_sticker(ai_mds)


def perfilInsta(update: Update, context: CallbackContext) -> None:
    proibidos = ["joedellaira","anne_kelly99","nayane_diast","4linefernades","kynha_marques"]
    resposta1 = update.message.reply_text("Peraê.")
    infos = ""
    nome = context.args[0]
    local_photos = abspath(f"./{nome}")
    
    if nome in proibidos and update.message.from_user.id != idYsrael:
        resposta1.edit_text("Não.")
        update.message.reply_sticker(haha)
        return
    
    try:
        app = instaloader.Instaloader(compress_json=False,dirname_pattern=local_photos)
    
        perfil = instaloader.Profile.from_username(app.context,nome)
    
        app.download_profiles([perfil],posts=False)
        chdir(nome)

        for c in listdir():
            if isfile(c):
                if c.endswith("profile_pic.jpg"):
                    foto = abspath(c)
                    
                if c.endswith(".json"):
                    
                    infos = json.load(open(c,"r"))
                    bio = infos['node']['biography'] if infos['node']['full_name'] != None else ""
                    nome_prof = infos['node']['full_name'] if infos['node']['full_name'] != None else ""
                    urlink = infos['node']['external_url'] if infos['node']['external_url'] != None else ""
    
        legenda = f"https://instagram.com/{nome}"
        legenda +="\n"
        legenda += nome_prof
        legenda +="\n"
        legenda += bio
        legenda +="\n"
        legenda += urlink
    
        if foto != "":
            resposta1.delete()
    
        update.message.reply_photo(photo=open(foto,'rb'),caption=legenda)
    
        chdir("../")
    
        shutil.rmtree(local_photos)
    except:
        resposta1.edit_text("Não consigo.")
        update.message.reply_sticker(ai_mds)