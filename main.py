import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salam! Bu @neisteyirsen_bot-dur. Nə istəyirsən?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Sən yazdın: " + message.text)

bot.polling()
