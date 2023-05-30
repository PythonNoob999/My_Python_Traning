# nedded libs
import telebot
from telebot import types,util
from decouple import config
import math
# Create a .env File and store the bot token in a variable
# and but the variable name here 👇
BOT_TOKEN = config("MATH_BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)
data = []
# bot commands
@bot.message_handler(commands = ["start", "help", "history", "calc", "factorial", "sqrt", "pow"])
# check what the user typed and reply to it
def math_bot(message):
    # splitting the user message to easily deal with it
    text = message.text.split()
    if text[0] == '/start':
        bot.reply_to(message, "Hello to Kerolis math bot")
    elif text[0] == '/help':
        bot.reply_to(message, "This bot is made by @kerolis55463\nthis bot do simple math opreations here's a list for all the opreations you can do\n/calc\n/factorial\n/sqrt\n/pow")
    elif text[0] == '/calc':
        try:
            result = eval(text[1])
            bot.reply_to(message, result)
        except:
            bot.reply_to(message, 'oops try vaild equation')
    elif text[0] == '/factorial':
         resultf = math.factorial(int(text[1]))
         bot.reply_to(message, resultf)
    elif text[0] == '/sqrt':
         results = math.sqrt(int(text[1]))
         bot.reply_to(message, results)
    elif text[0] == '/pow':
        x = text[1].split('^')
        resultp = math.pow(int(x[0]), int(x[1]))
        bot.reply_to(message, resultp)
        
        
# starting the bot infinitly
bot.infinity_polling(allowed_updates=util.update_types)
    
