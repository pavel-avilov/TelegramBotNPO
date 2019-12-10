import telebot

import parse

TOKEN = '1046403625:AAG2y-Tk5OvYsVqW8PMIBC8G9EgZgDojcxQ'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id,
                     'Привет, я Бот Некомерческих Организация. Если отправите мне ИНН интересующей Вас некомерческой организации, то я дам Вам небольшую справку о ней)')


@bot.message_handler(commands=['help'])
def start_handler(message):
    bot.send_message(message.chat.id,
                     'Просто отправите мне ИНН интересующей Вас некомерческой организации)')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if len(text) == 10 and text.isdigit():
        parse.parse(text)
        message_send = ''
        if 'fail' in parse.data:
            bot.send_message(chat_id, 'Организация с таким ИНН не найдена')
        else:
            for key, value in parse.data.items():
                message_send += str(key) + ' - ' + str(value) + '\n'
            bot.send_message(chat_id, message_send)
    else:
        bot.send_message(chat_id, 'Вы ввели некорректный ИНН')


bot.polling()
