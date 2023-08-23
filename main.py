# n=input().split()
# s=1
# i=int(n[0])
# for j in range(1,3):
#   if i!=int(n[j]):
#     s+=1
# # print(s)
# n=input().split()
# a=int(n[0])
# for i in range(1,3):
#   if int(n[i])>int(a):
#     a=n[i]
# print(a)
#
# son = {
#     1: "bir",
#     2: "ikki",
#     3: "uch",
#     4: "to’rt",
#     5: "besh",
#     6: "olti",
#     7: "yetti",
#     8: "sakkiz",
#     9: "to’qqiz",
#     10: "o’n",
#     20: "yigirma",
#     30: "o’ttiz",
#     40: "qirq",
#     50: "ellik",
#     60: "oltmish",
#     70: "yetmish",
#     80: "sakson",
#     90: "to’qson",
#     100: "bir yuz",
#     200: "ikki yuz",
#     300: "uch yuz",
#     400: "to`rt yuz",
#     500: "besh yuz",
#     600: "olti yuz",
#     700: "yetti yuz",
#     800: "sakkiz yuz",
#     900: "to`qqiz yuz",
#     1000: "bir ming"
#
# }
# s=""
# n = int(input()) #48
# if n==1000:
#   print(son.get(n))
# elif n==0:
#     print("nol")
# else:
#    m=son.get(n%1000//100*100)
#    if m==None:
#        s+=""
#    else:
#        s+=m+" "
#    q=son.get(n%1000//10%10*10)
#    if q==None:
#        s+=""
#    else:
#        s+=q+" "
#    s+=son.get(n%10,"")
# print(s)

# import sinov as s
# avtolar=s.avto_kirit()
# for avto in avtolar:
#     print(avto["rangi"], avto["rusumi"], avto["narxi"])
# def avto_info(rusumi, rangi, narxi):
#     """Avtomobil malumotlarini lug`at shaklida chiqaruvchi funksiya"""
#     info={
#         "rusumi": rusumi,
#         "rangi": rangi,
#         "narxi": narxi
#     }
#     return info
# def avto_kirit():
#     avto=[]
#     rusumi=input("Rusumi: ")
#     rangi=input("Rangi: ")
#     narxi=input("Narxi: ")
#     avto.append(avto_info(rusumi, rangi, narxi))
#     return avto
# def avto_print(avto_info):
#     print(f"{avto_kirit([1])} {avto_kirit([0])}.Narxi {avto_kirit([2])}")

# import random
# from sinov import play
# user=play()
# print(f"Tabriklaymiz! {len(user)} ta urinishda topdingiz")

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

