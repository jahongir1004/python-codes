from transliterate import to_latin, to_cyrillic
import telebot
TOKEN="6024414386:AAGAimPld1jvptyRtXWIZ0EVCaUt1gZYNpY"

bot = telebot.TeleBot(TOKEN, parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalomu alaykum.Xush kelibsiz!"
    javob+="\nMatn kiritng: "
    bot.reply_to(message, javob)
@bot.message_handler(func=lambda message: True)
def echo_all(massage):
    msg=massage.text
    answer=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    
    bot.reply_to(massage, answer(msg))    
bot.polling()

