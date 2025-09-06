import telebot

# Встав свій токен, який ти отримав від BotFather
TOKEN = "ТВОЙ_ТОКЕН_СЮДИ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт 👋! Це мій NFT бот.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
