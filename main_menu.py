from telegram import Update
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, PrefixHandler, CallbackContext

# Funcoes de execucao
def start(update: Update, context: CallbackContext) -> None:
    mensagem = "Bem vindo {}!!!\n".format(update.effective_user.first_name)
    mensagem += "Confira a lista de comandos validos:\n"
    mensagem += "/start - Envia a mensagem inicial de boas vindas\n"
    mensagem += "/r - faz rolagem de dados, exemplo: /r 1d20\n"
    mensagem += "/help <comando> - exibe instruções como usar determinado comando\n"
    mensagem += "/insta <perfil> - Envia a foto do perfil desejado\n"
    mensagem += "/buscaig <perfil> - Envia uma lista com no máximo 10 resultados de perfis do termo buscado\n"
    mensagem += "\nDesejo-lhe novamente as boas vindas e divirta-se!!!"
    update.message.reply_text(mensagem)