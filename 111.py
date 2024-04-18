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
    file = open('датчик.json', 'r', encoding='utf-8')
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

        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Кислородно-газовый', callback_data='Кислородно-газовый')
        button2 = types.InlineKeyboardButton(text='АСУТП', callback_data='АСУТП')
        button3 = types.InlineKeyboardButton(text='Колесобандажный', callback_data='Колесобандажный')
        button4 = types.InlineKeyboardButton(text='Конверторный', callback_data='Конверторный')
        button5 = types.InlineKeyboardButton(text='УЖДТ', callback_data='УЖДТ')

        keyboard.add(button1, button2, button3, button4, button5)

        bot.send_message(message.from_user.id, text='Добро пожаловать!')
        bot.send_message(message.from_user.id, text='Выберите цех, из которого вы хотите получить данные с датчиков', reply_markup=keyboard)




    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        global active_department

        file = open('датчик.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        departments = []
        for i in range(len(data)):
            if data[i]['department'] not in departments:
                departments.append(data[i]['department'])
        for department in departments:
            if call.data == department:
                result["department"] = department
                active_department = department
                bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                keyboard2 = types.InlineKeyboardMarkup()
                button1_2 = types.InlineKeyboardButton(text='Лента №1', callback_data='Лента №1')
                button2_2 = types.InlineKeyboardButton(text='Лента №2', callback_data='Лента №2')
                button3_2 = types.InlineKeyboardButton(text='Лента №3', callback_data='Лента №3')
                button4_2 = types.InlineKeyboardButton(text='Лента №4', callback_data='Лента №4')
                button5_2 = types.InlineKeyboardButton(text='Лента №5', callback_data='Лента №5')
                keyboard2.add(button1_2, button2_2, button3_2, button4_2, button5_2)
                bot.send_message(call.from_user.id, text='Выберите ленту для просмотра', reply_markup=keyboard2)
                break

        file = open('датчик.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        lentas = []

        for i in range(len(data)):
            if data[i]['department'] not in departments:
                departments.append(data[i]['department'])
            elif active_department == data[i]['department']:
                lentas.append(data[i]['lenta'])

        if call.data.startswith('Лента'):
            for lenta in lentas:
                if call.data == lenta:
                    result['lenta'] = lenta
                    bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                    keyboard3 = types.InlineKeyboardMarkup()
                    button1_3 = types.InlineKeyboardButton(text='Датчик электричества ', callback_data='Датчик электричества')
                    button2_3 = types.InlineKeyboardButton(text='Датчик воды', callback_data='Датчик воды')
                    button3_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик давления')
                    button4_3 = types.InlineKeyboardButton(text='Датчик температуры', callback_data='Датчик температуры')
                    button5_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик температуры')
                    keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
                    bot.send_message(call.from_user.id, text='Выберите вид датчика', reply_markup=keyboard3)

                elif call.data == 'лента №2':
                    bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                    keyboard3 = types.InlineKeyboardMarkup()
                    button1_3 = types.InlineKeyboardButton(text='Датчик электричества ', callback_data='Датчик электричества')
                    button2_3 = types.InlineKeyboardButton(text='Датчик воды', callback_data='Датчик воды')
                    button3_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик давления')
                    button4_3 = types.InlineKeyboardButton(text='Датчик температуры', callback_data='Датчик температуры')
                    button5_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик температуры')
                    keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
                    bot.send_message(call.from_user.id, text='Выберите вид датчика', reply_markup=keyboard3)

                elif call.data == 'лента №3':
                    bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                    keyboard3 = types.InlineKeyboardMarkup()
                    button1_3 = types.InlineKeyboardButton(text='Датчик электричества ', callback_data='Датчик электричества')
                    button2_3 = types.InlineKeyboardButton(text='Датчик воды', callback_data='Датчик воды')
                    button3_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик давления')
                    button4_3 = types.InlineKeyboardButton(text='Датчик температуры', callback_data='Датчик температуры')
                    button5_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик температуры')
                    keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
                    bot.send_message(call.from_user.id, text='Выберите вид датчика', reply_markup=keyboard3)

                elif call.data == 'лента №4':
                    bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                    keyboard3 = types.InlineKeyboardMarkup()
                    button1_3 = types.InlineKeyboardButton(text='Датчик электричества ', callback_data='Датчик электричества')
                    button2_3 = types.InlineKeyboardButton(text='Датчик воды', callback_data='Датчик воды')
                    button3_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик давления')
                    button4_3 = types.InlineKeyboardButton(text='Датчик температуры', callback_data='Датчик температуры')
                    button5_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик температуры')
                    keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
                    bot.send_message(call.from_user.id, text='Выберите вид датчика', reply_markup=keyboard3)

                else:
                    bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                    keyboard3 = types.InlineKeyboardMarkup()
                    button1_3 = types.InlineKeyboardButton(text='Датчик электричества ', callback_data='Датчик электричества')
                    button2_3 = types.InlineKeyboardButton(text='Датчик воды', callback_data='Датчик воды')
                    button3_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик давления')
                    button4_3 = types.InlineKeyboardButton(text='Датчик температуры', callback_data='Датчик температуры')
                    button5_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик температуры')
                    keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
                    bot.send_message(call.from_user.id, text='Выберите вид датчика', reply_markup=keyboard3)

        file = open('датчик.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        vidi_datchikov = []

        for i in range(len(data)):
            if data[i]['department'] not in departments:
                departments.append(data[i]['department'])
            elif active_department == data[i]['department']:
                vidi_datchikov.append(data[i]['vid_datchika'])

        if call.data.startswith('Датчик №'):
            file = open('датчик.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            datchiki = []

            for i in range(len(data)):
                if data[i]['department'] not in departments:
                    departments.append(data[i]['department'])
                elif active_department == data[i]['department']:
                    datchiki.append(data[i]['datchik'])

            for datchik in datchiki:
                if call.data == datchik:
                    result['datchik'] = datchik
                    bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                    keyboard4 = types.InlineKeyboardMarkup()
                    button1_4 = types.InlineKeyboardButton(text='Ввод даты самостоятельно', callback_data='Ввод даты самостоятельно')
                    button2_4 = types.InlineKeyboardButton(text='Получение данных за две недели', callback_data='Получение данных за две недели')
                    keyboard4.add(button1_4, button2_4)
                    bot.send_message(message.from_user.id, text='Выберите дату для вывода информации', reply_markup=keyboard4)

        if call.data.startswith('Ввод даты самостоятельно'):
            bot.send_message(message.from_user.id, text='Выберите дату для вывода информации ггг-мм-дд')
            bot.register_next_step_handler(call.message, get_data_for_date)

        elif call.data.startswith('Получение данных за две недели'):
            bot.send_message(message.from_user.id, text='Все показания за две недели')
            file = open('датчик.json', 'r', encoding='utf-8')
            datas = json.load(file)
            file.close()
            text = ''
            for data in datas:
                if data['department'] == active_department:
                    text += '\nПоказатели:' + str(data['value']) + '\n'
                    bot.send_message(call.from_user.id, text=text)



        elif call.data.startswith('Датчик'):
            for vid_datchika in vidi_datchikov:
                if call.data == vid_datchika:
                    result['vid_datchika'] = vid_datchika
                    bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                    keyboard3 = types.InlineKeyboardMarkup()
                    button1_3 = types.InlineKeyboardButton(text='Датчик №1 ',callback_data='Датчик №1')
                    button2_3 = types.InlineKeyboardButton(text='Датчик №2', callback_data='Датчик №2')
                    button3_3 = types.InlineKeyboardButton(text='Датчик №3', callback_data='Датчик №3')
                    button4_3 = types.InlineKeyboardButton(text='Датчик №4', callback_data='Датчик №4')
                    button5_3 = types.InlineKeyboardButton(text='Датчик №5', callback_data='Датчик №5')
                    keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
                    bot.send_message(call.from_user.id, text='Выберите номер датчика', reply_markup=keyboard3)
                    break

                elif call.data == 'Датчик воды':
                    bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                    keyboard3 = types.InlineKeyboardMarkup()
                    button1_3 = types.InlineKeyboardButton(text='Датчик №1 ',callback_data='Датчик №1')
                    button2_3 = types.InlineKeyboardButton(text='Датчик №2', callback_data='Датчик №2')
                    button3_3 = types.InlineKeyboardButton(text='Датчик №3', callback_data='Датчик №3')
                    button4_3 = types.InlineKeyboardButton(text='Датчик №4', callback_data='Датчик №4')
                    button5_3 = types.InlineKeyboardButton(text='Датчик №5', callback_data='Датчик №5')
                    keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
                    bot.send_message(call.from_user.id, text='Выберите номер датчика', reply_markup=keyboard3)
                    break

                elif call.data == 'Датчик давления':
                    bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                    keyboard3 = types.InlineKeyboardMarkup()
                    button1_3 = types.InlineKeyboardButton(text='Датчик №1 ',callback_data='Датчик №1')
                    button2_3 = types.InlineKeyboardButton(text='Датчик №2', callback_data='Датчик №2')
                    button3_3 = types.InlineKeyboardButton(text='Датчик №3', callback_data='Датчик №3')
                    button4_3 = types.InlineKeyboardButton(text='Датчик №4', callback_data='Датчик №4')
                    button5_3 = types.InlineKeyboardButton(text='Датчик №5', callback_data='Датчик №5')
                    keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
                    bot.send_message(call.from_user.id, text='Выберите номер датчика', reply_markup=keyboard3)
                    break

                elif call.data == 'Датчик температуры':
                    bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                    keyboard3 = types.InlineKeyboardMarkup()
                    button1_3 = types.InlineKeyboardButton(text='Датчик №1 ',callback_data='Датчик №1')
                    button2_3 = types.InlineKeyboardButton(text='Датчик №2', callback_data='Датчик №2')
                    button3_3 = types.InlineKeyboardButton(text='Датчик №3', callback_data='Датчик №3')
                    button4_3 = types.InlineKeyboardButton(text='Датчик №4', callback_data='Датчик №4')
                    button5_3 = types.InlineKeyboardButton(text='Датчик №5', callback_data='Датчик №5')
                    keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
                    bot.send_message(call.from_user.id, text='Выберите номер датчика', reply_markup=keyboard3)
                    break

                else:
                    bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                    keyboard3 = types.InlineKeyboardMarkup()
                    button1_3 = types.InlineKeyboardButton(text='Датчик №1 ',callback_data='Датчик №1')
                    button2_3 = types.InlineKeyboardButton(text='Датчик №2', callback_data='Датчик №2')
                    button3_3 = types.InlineKeyboardButton(text='Датчик №3', callback_data='Датчик №3')
                    button4_3 = types.InlineKeyboardButton(text='Датчик №4', callback_data='Датчик №4')
                    button5_3 = types.InlineKeyboardButton(text='Датчик №5', callback_data='Датчик №5')
                    keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
                    bot.send_message(call.from_user.id, text='Выберите номер датчика', reply_markup=keyboard3)
                    break
            print(result)
















bot.polling(none_stop=True, interval=0)


