import telebot

TOKEN = "8005297468:AAG1XLRaA9ubHne1XbeZoes18fB9GAFeWrQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "أهلاً بيك بـ بوت نمبر ون - كلشي متوفر!")

bot.polling()
