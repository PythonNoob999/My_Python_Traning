#chat bot

import telebot
from decouple import config
from telebot import types,util

# Creatin the Bot


BOT_TOKEN = config('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

text_message = {
    "welcome":
        "im test bot",
    "new_user":
        u"hello {name}",
    "bye_noob":
        u"bye {name} nerd"
}

@bot.message_handler(commands = ["start", "help", "hi"])
def startbot(message):
    bot.send_message(message.chat.id, text_message["welcome"])

# greeting the new members
@bot.chat_member_handler()

def handleuserupdate(message:types.ChatMemberUpdated):
    newresponse = message.new_chat_member
    if newresponse.status == "member":
        # greeting by name
        bot.send_message(message.chat.id, text_message["new_user"].format(name=newresponse.user.first_name))

# saying good bye        
    if newresponse.status == "left":
        bot.send_message(message.chat.id, text_message["bye_noob"].format(name=newresponse.user.first_name))


# making the bot not join any group or get added

@bot.my_chat_member_handler()

def leave(message:types.ChatMemberUpdated):
    update = message.new_chat_member
    if update.status == "member":
        bot.leave_chat(message.chat.id)

# listening to group members

@bot.message_handler(func=lambda m:True)

def calc(message):
        equation = message.text
        x = eval(equation)
        if True:
            bot.reply_to(message,x)
        
        
# checking for new message    

bot.infinity_polling(allowed_updates=util.update_types)

