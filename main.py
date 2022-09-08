from telebot import TeleBot
import time
import requests

app = TeleBot('5748453485:AAHyrDr2j9yEvvEBE3RN2fDw69GY2cwcqqo')
url = "https://api.telegram.org/bot5748453485:AAHyrDr2j9yEvvEBE3RN2fDw69GY2cwcqqo/getupdates"
requesição = requests.get(url)
print(requesição.json())

###############################################

def verificar(mensagem):
    if mensagem.text == "Olá!" or mensagem.text == "olá!" or mensagem.text == "Ola!" or mensagem.text == "ola" or mensagem.text == "olá" or mensagem.text == "Oi!" or mensagem.text == "Oi" or mensagem.text == "oi":
        return True

###############################################

@app.message_handler(func=verificar)
def responder(mensagem):
    app.reply_to(mensagem, "Oi!")

###############################################

@app.message_handler(commands=["/start"])
def responder(mensagem):
    app.reply_to(mensagem, "Oi, digite /help para ver os meus comandos!")
    
###############################################

@app.message_handler(commands=["help"])
def responder(mensagem):
    texto = """Olá, eu sou a Julis😘, e seja bem-vindo a minha lista de comandos!✨
    
    /help   | Mostra está mensagem
    /start  | Mostra uma mensagem
    /time   | Mostra a hora
    /day    | Mostra o dia
    /hour   | Mostra a hora
    /month  | Mostra o mês
    /year   | Mostra o ano
    /utctime| Mostra o tempo UTC
    /dayweek| Mostra o dia da semana
    /adate  | Mostra a data apropriada
    /hour12 | Mostra o tem no formato 12h
    /ampm   | Mostra o equivalente ao am e pm
    
Estes são todos os meus comandos😎, se gostou, vá para o github do meu criador 🤩: https://ww.github.com/angelofran
Lá você pode encontrar o meu código fonte, Obrigado💖"""

    app.reply_to(mensagem, texto)

###############################################

@app.message_handler(commands = ["time"])
def responder(mensagem):
    tempo = f'{time.strftime("Data actual: %H:%M, %d de %B de %Y")}'
    app.reply_to(mensagem, tempo)

###############################################

@app.message_handler(commands = ["day"])
def responder(mensagem):
    tempo = f'{time.strftime("Hoje é dia: %d")}'
    app.reply_to(mensagem, tempo)

###############################################

@app.message_handler(commands = ["hour"])
def responder(mensagem):
    tempo = f'{time.strftime("%H:%M:%S")}'
    app.reply_to(mensagem, tempo)

###############################################

@app.message_handler(commands = ["month"])
def responder(mensagem):
    tempo = f'{time.strftime("%b/%B/%m")}'
    app.reply_to(mensagem, tempo)

###############################################

@app.message_handler(commands = ["year"])
def responder(mensagem):
    tempo = f'{time.strftime("%Y")}'
    app.reply_to(mensagem, tempo)

###############################################

@app.message_handler(commands = ["utctime"])
def responder(mensagem):
    tempo = f'{time.strftime("%z")}'
    app.reply_to(mensagem, tempo)

###############################################

@app.message_handler(commands = ["dayweek"])
def responder(mensagem):
    tempo = f'{time.strftime("%A/%a")}'
    app.reply_to(mensagem, tempo)

###############################################

@app.message_handler(commands = ["adate"])
def responder(mensagem):
    tempo = f'{time.strftime("%c")}'
    app.reply_to(mensagem, tempo)
    
###############################################

@app.message_handler(commands = ["hour[1-12]"])
def responder(mensagem):
    tempo = f'{time.strftime("%I")}'
    app.reply_to(mensagem, tempo)

###############################################

@app.message_handler(commands = ["ampm"])
def responder(mensagem):
    tempo = f'{time.strftime("%p")}'
    app.reply_to(mensagem, tempo)

###############################################

app.polling()
