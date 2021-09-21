from telegram import Update
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, PrefixHandler, CallbackContext

def help(update: Update, context: CallbackContext):
    for arg in context.args:
        update.message.reply_text(search_help(arg))

def search_help(type_help):
    if type_help == "start":
        return  "O comando /{} envia a mensagem inicial de boas vindas".format(type_help)
    
    elif type_help == "help":
        return  """
    O comando /{} exibe instruções como usar determinado comando.

Exemplo: /help <comando>
    """.format(type_help)

    elif type_help == "insta":
        return  """
    O comando /{} envia a foto do perfil do Instagram desejado.

Exemplo: /insta <perfil>
    """.format(type_help)

    elif type_help == "buscaig":
        return  """
    O comando /{} envia uma lista com no máximo 10 resultados de perfis do termo buscado.

Exemplo: /insta <perfil>
    """.format(type_help)

    elif type_help == "r":
        return  """
    O comando /{} faz rolagem de dados, exemplo: /r 1d20
E pode fazer rolagens mais elaboradas com somas e mais de um tipo de dado.

Exemplos:

        /r 1d20+2d4
        /r 5+1d20
        /r 5+1d20+2d4

Nota: No momento não está funcionando a operação subtração, recomenda-se também que números que se deseja somar a rolagem sejam colocados antes dos dados.
""".format(type_help)
    
    else:
        return  "O comando /{} não é reconhecido, digite um comando válido".format(type_help)