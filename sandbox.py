from random import choice
from os import chdir, getcwd, listdir, remove
from os.path import isfile,abspath
import json
import shutil
import instaloader
import requests

app = instaloader.Instaloader()
app.login("seg_runeterra","learsy10")
busca = instaloader.TopSearchResults(app.context,"pele")

resultados = list(busca.get_profiles())

for post in resultados[0:10]:
    print(f"{post.username}  ({'Privado' if post.is_private else 'Aberto'}) {'✔️' if post.is_verified else ''}")