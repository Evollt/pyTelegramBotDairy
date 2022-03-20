# импорт библиотек и токена, который находится в файле config.py
from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
import emoji
from parser import page_all_a

# задаем бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# создание кнопок и всего этого при команде старт
@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, emoji.emojize(':thumbs_up:') + 'Привет, я бот, который будет показывать тебе колледжное расписание. Рад тебя видеть. Выбери что тебе нужно.', reply_markup=kb.markup_function)

# помощь пользователю
@dp.message_handler(commands=['help'])
async def process_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'Напишите команду /start, а дальше все станет интуитивно понятно')

# при отправке сообщения
@dp.message_handler()
async def process_reply(message: types.Message):
    if message.text.lower() == 'посмотреть расписание':
        await bot.send_message(message.from_user.id, 'Твое расписание: ' + page_all_a[338].get('href'))
        await bot.send_message(message.from_user.id, 'Твое расписание: ' + page_all_a[340].get('href'))
        await bot.send_message(message.from_user.id, 'Твое расписание: ' + page_all_a[346].get('href'))
    
    if message.text.lower() == 'посмотреть преподовательское расписание':
        # page_all_a это переменная с парсера находится по индексу тега a
        await bot.send_message(message.from_user.id, 'Расписание преподавателей: ' + page_all_a[339].get('href'))
        await bot.send_message(message.from_user.id, 'Расписание преподавателей: ' + page_all_a[343].get('href'))
        await bot.send_message(message.from_user.id, 'Расписание преподавателей: ' + page_all_a[349].get('href'))
    
    if message.text.lower() == 'посмотреть ссылкy на дистанционное обучение':
        await bot.send_message(message.from_user.id, 'Ссылка на дистанционное обучение: ' + page_all_a[334].get('href'))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)