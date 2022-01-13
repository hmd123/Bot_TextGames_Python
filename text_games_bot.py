import os 
import telebot
from telebot import types

import lab_game as lg


lab = None

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN1']) #salva na variavel


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    global lab
    bot.send_message(message.chat.id, "Olá, bem-vindo ao bot!")
    lab = False
    botaoMenu(message)

    
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "lab":
            start_lab(call.message)
            
        
@bot.message_handler(commands=['labirinto'])
def start_lab(message):
    global lab
    lab = True
    lg.engine(message)
    
   
@bot.message_handler(func=lambda message: True)    
def listen(message):
    global lab
    if lab == True:
        lg.direcoes(message)
        if lg.checaCondSaida():
            lab = False
            send_welcome(message)


def botaoMenu(message):
    markup = types.InlineKeyboardMarkup()
    itembte = types.InlineKeyboardButton("Labirinto", callback_data='lab')
    itembtd = types.InlineKeyboardButton("Outros \n(ainda produzindo)", callback_data='lab')
    markup.row(itembte)
    markup.row(itembtd)
    bot.send_message(message.chat.id, "Escolha o jogo: ", reply_markup=markup)
    
bot.polling(none_stop=True)
