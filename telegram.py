import telebot
import webbrowser
import sqlite3
from telebot import types

bot = telebot.TeleBot('7350988824:AAEhAlRx0ZtGLAN8klaeZ1HF2mbh9PMV3fI')


# Подключение к базе данных SQLite
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создание таблицы для хранения информации о пользователях
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (user_id INTEGER PRIMARY KEY, username TEXT)''')
conn.commit()

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Чем могу вам помочь?')

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://ya.ru/images/search?from=tabbar&text=%D0%BC%D0%B0%D0%B3%D0%B8%D1%8F')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Удалить фото")
    item2 = types.KeyboardButton("Добавить текст")
    item3 = types.KeyboardButton("Перейти на сайт")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Привет! Добро пожаловать в Хогвартс. Здесь ты найдёшь для себя увлекательную и интересную информацию, которая надеюсь тебе поможет стать магистром мира!", reply_markup=markup)


    markup = types.InlineKeyboardMarkup()
    btn_site = types.InlineKeyboardButton(text='Перейти на сайт',
                                          url='https://yandex.ru/images/search?from=tabbar&text=%D0%BC%D0%B0%D0%B3%D0%B8%D1%8F')
    markup.add(btn_site)

    # Отправляем сообщение с кнопкой для перехода на сайт
    bot.send_message(message.chat.id,
                     'Для начала предлагаю тебе ознакомиться с нашим сайтом. Переходи по ссылке и вперёд!',
                     reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Перейти на сайт"))
    markup.add(types.KeyboardButton("Удалить фото"))
    markup.add(types.KeyboardButton("Добавить текст"))

# Запускаем бота
bot.polling(none_stop=True)
