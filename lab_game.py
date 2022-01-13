import os
import telebot
from telebot import types
import textos_labirinto as tl

arvore = None
opprov1 = None
opprov2 = None
condSaida = 0
ativa_pulo = 0

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN1']) #salva na variavel

def engine(message):
    global arvore
    global condSaida

    ativa_pulo = 0
    condSaida = 0
    arvore = tl.lab_arvore()
    arvore.arruma_arvore()
    bot.reply_to(message, "Vamos começar!!")
    opcoes()
    primBotao(message)

#func lambda
def direcoes(message):
    global arvore
    global opprov1
    global opprov2
    global condSaida
    global ativa_pulo

    if message.text == "JOGO DO LABIRINTO":
        bot.send_message(message.chat.id, tl.init_jogolabirinto)
        botaoReinicia(message)
    if message.text == "Reiniciar Jogo":
        engine(message)
    elif message.text == "Sair":
        condSaida = 1
    else:
        opcoes()
        if message.text == opprov1:
            arvore = arvore.avanca_arvore(1)
        elif message.text == opprov2:
            arvore = arvore.avanca_arvore(2)
            if ativa_pulo == 2: #ativar teletransporte e volta pro inicio
                ativa_pulo = 0
                bot.send_message(message.chat.id, arvore.val)
                engine(message)
                return
            elif ativa_pulo == 1: #ativa um pulo que vai de um nó pra outro de diferentes pais
                ativa_pulo = 0
                pulo_dimensional()


        opcoes()
        if opprov1 == None and opprov2 == None:
            bot.send_message(message.chat.id, arvore.val)
            botaoReinicia(message)
        else:
            primBotao(message)


def primBotao(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembte = types.KeyboardButton(opprov1)
    itembtd = types.KeyboardButton(opprov2)
    markup.row(itembte,itembtd)
    bot.send_message(message.chat.id, arvore.val, reply_markup=markup)


def umBotao(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembte = types.KeyboardButton(opprov1)
    markup.row(itembte)
    bot.send_message(message.chat.id, arvore.val, reply_markup=markup)

def botaoReinicia(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembte = types.KeyboardButton("Reiniciar Jogo")
    itembtd = types.KeyboardButton("Sair")
    markup.row(itembte,itembtd)
    bot.send_message(message.chat.id, "Reiniciar Jogo?", reply_markup=markup)



def opcoes():
    global arvore
    global opprov1
    global opprov2
    global ativa_pulo

    op1 = "Esquerda"
    op2 = "Direita"
    op3 = "Sim"
    op4 = "Não"
    op5 = "Vermelho"
    op6 = "Azul"
    op7 = "Carinho"
    op8 = "Chutar"
    op9 = "Sim, eu quero muito muito muito entrar para a Universidade"
    op10 = "TELETRANSPORTADOR"
    op11 = "CAMINHO QUE NÃO PODE"


    if(arvore.opcoes == 0):
        opprov1 = None
        opprov2 = None
    elif(arvore.opcoes == 1):
        opprov1 = op1
        opprov2 = op2
    elif(arvore.opcoes == 2):
        opprov1 = op3
        opprov2 = op4
    elif(arvore.opcoes == 3):
        opprov1 = op5
        opprov2 = op6
    elif(arvore.opcoes == 4):
        opprov1 = op7
        opprov2 = op8
    elif(arvore.opcoes == 5):
        opprov1 = op9
        opprov2 = op4
    elif(arvore.opcoes == 6):
        opprov1 = op1
        opprov2 = op10
        ativa_pulo = 2
    elif(arvore.opcoes == 7):
        opprov1 = op11
        opprov2 = op2
        ativa_pulo = 1

def checaCondSaida():
    global condSaida

    if condSaida == 1:
        return True
    else:
        return False

def pulo_dimensional(): #velha gambiarra
    global arvore
    arvore = tl.lab_arvore()
    arvore.arruma_arvore()
    arvore = arvore.avanca_arvore(2)
    arvore = arvore.avanca_arvore(2)
    arvore = arvore.avanca_arvore(2)
    arvore = arvore.avanca_arvore(2)
