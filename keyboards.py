from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
# создание кнопок
markup_function = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Посмотреть расписание')).add(KeyboardButton('Посмотреть преподовательское расписание')).add('Посмотреть ссылкy на дистанционное обучение')