import json
import telebot
from telebot import types
token = '7123532905:AAHCw-orSkIET0JSmSqPgNHb3rgtwXhGKtA'
bot = telebot.TeleBot(token)

active_department = ''
result = {
    "department": "",
    "lenta": "",
    "vid_datchika": "",
    "datchik": "",
    "date": "",
}

def get_data_for_date(message):
    file = open('data.json', 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    for i in range(len(data)):
        if data[i]['date'] == message.text:
            result['date'] = message.text
        else:
            message.text = message.text[::-1]
            message.text = message.text.replace('.', ('-'))
            result['date'] = message.text


            



@bot.message_handler(content_types=['text'])

def get_message(message):
    if message.text == '/start':

        bot.set_my_commands(
            commands=[
                types.BotCommand('/start', 'Запуск бота'),
                types.BotCommand('/dance', 'Получить танец'),
                types.BotCommand('/bomb', 'Не нажимать')
            ],
            scope=types.BotCommandScopeChat(message.chat.id)
        )

        file = open('data.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        keyboard = types.InlineKeyboardMarkup()
        for department in list(data.keys()):
            button = types.InlineKeyboardButton(text=department, callback_data='department_'+department)
            keyboard.add(button)
        bot.send_message(message.from_user.id, text='Добро пожаловать!')
        bot.send_message(message.from_user.id, text='Выберите цех, из которого вы хотите получить данные с датчиков', reply_markup=keyboard)




    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        global active_department, active_lenta, active_vid_datchika, active_datchik


        if call.data.startswith('department_'):
            active_department = call.data.split('_')[1]
            file = open('data.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            keyboard2 = types.InlineKeyboardMarkup()
            for lenta in list(data[active_department].keys()):
                button1_2 = types.InlineKeyboardButton(text=lenta, callback_data='lenta_'+lenta)
                keyboard2.add(button1_2)
            bot.send_message(message.from_user.id, text='Выберите ленту для просмотра', reply_markup=keyboard2)

        # АУСТП|Лента 1



        if call.data.startswith('lenta_'):
            active_lenta = call.data.split('_')[1]
            file = open('data.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            keyboard3 = types.InlineKeyboardMarkup()
            for vid_datchika in list(data[active_department][active_lenta].keys()):
                button1_3 = types.InlineKeyboardButton(text=vid_datchika, callback_data='vid_datchika_'+vid_datchika)
                keyboard3.add(button1_3)
            bot.send_message(message.from_user.id, text='Выберите вид датчика', reply_markup=keyboard3)



        if call.data.startswith('vid_datchika_'):
            active_vid_datchika = call.data.split('_')[2]
            file = open('data.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            keyboard4 = types.InlineKeyboardMarkup()
            for datchik in list(data[active_department][active_lenta][active_vid_datchika].keys()):
                button1_4 = types.InlineKeyboardButton(text=datchik, callback_data='datchik'+datchik)
                keyboard4.add(button1_4)
            bot.send_message(message.from_user.id, text='Выберите номер датчика', reply_markup=keyboard4)



        if call.data.startswith('datchik_'):
            active_datchik = call.data.split('_')[1]
            file = open('data.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            keyboard5 = types.InlineKeyboardMarkup()
            for date in list(data[active_department][active_lenta][active_vid_datchika][active_datchik].keys()):
                button1_5 = types.InlineKeyboardButton(text=date, callback_data='date'+date)
                keyboard5.add(button1_5)
            bot.send_message(message.from_user.id, text='Выберите дату для вывода информации', reply_markup=keyboard5)

            keyboard6 = types.InlineKeyboardMarkup()
            button1_6 = types.InlineKeyboardButton(text='Ввод даты самостоятельно', callback_data='Ввод даты самостоятельно')
            button2_6 = types.InlineKeyboardButton(text='Получение данных за две недели', callback_data='Получение данных за две недели')
            keyboard6.add(button1_6, button2_6)
            bot.send_message(message.from_user.id, text='Выберите дату для вывода информации', reply_markup=keyboard6)


















        #     for datchik in datchiki:
        #         if call.data == datchik:
        #             result['datchik'] = datchik
        #             bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
        #             keyboard4 = types.InlineKeyboardMarkup()
        #             button1_4 = types.InlineKeyboardButton(text='Ввод даты самостоятельно', callback_data='Ввод даты самостоятельно')
        #             button2_4 = types.InlineKeyboardButton(text='Получение данных за две недели', callback_data='Получение данных за две недели')
        #             keyboard4.add(button1_4, button2_4)
        #             bot.send_message(message.from_user.id, text='Выберите дату для вывода информации', reply_markup=keyboard4)
        #
        # if call.data.startswith('Ввод даты самостоятельно'):
        #     bot.send_message(message.from_user.id, text='Выберите дату для вывода информации ггг-мм-дд')
        #     bot.register_next_step_handler(call.message, get_data_for_date)
        #
        # elif call.data.startswith('Получение данных за две недели'):
        #     bot.send_message(message.from_user.id, text='Все показания за две недели')
        #     file = open('датчик.json', 'r', encoding='utf-8')
        #     datas = json.load(file)
        #     file.close()
        #     text = ''
        #     for data in datas:
        #         if data['department'] == active_department:
        #             text += '\nПоказатели:' + str(data['value']) + '\n'
        #             bot.send_message(call.from_user.id, text=text)
        #
        #
        #


bot.polling(none_stop=True, interval=0)


