import telebot
import os

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot အလုပ်လုပ်နေပါပြီ။")

bot.polling()
