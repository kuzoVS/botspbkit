import logging
from aiogram import Bot, Dispatcher, executor, types
import knopki as nav
import parser as pr
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
import sqlite as s
from sqlite import conn, cursor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

grpi = ['121', '122', '123', '124', '125', '126', '127', '21', '22', '211', '212', '213', '214', '215', '216', '11', '12', '301', '302', '303',
          '304', '305', '306', '1', '2', '491', '492', '493', '494', '495', '496']

# tokenb = os.getenv("TOKEN")
tokenb = ()
bot = Bot(token=tokenb)
dp = Dispatcher(bot, storage=MemoryStorage())
num = True

class UserState(StatesGroup):
    chgroup = State()
    strt = State()

@dp.message_handler(commands=['start'])
async def startcmd(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет')
    grn = message.text
    us_id = message.from_user.id
    username = message.from_user.username
    if s.getTrue(user_id=us_id) is True and s.getName(conn=conn, user_id=us_id) is None:
        await message.answer('Вы зарегистрированы, но забыли указать номер группы.\n Введите номер своей группы')
        await UserState.chgroup.set()
    elif s.getTrue(user_id=us_id) is True and s.getName(conn=conn, user_id=us_id) is not None:
        await message.answer('Вы зарегистрированы!\n', reply_markup=nav.mainMenu)
    elif s.getTrue(user_id=us_id) is False:
        await message.answer(' Вы не зарегистрированы!\n Введите номер своей группы')
        await UserState.strt.set()
@dp.message_handler(state=UserState.strt)
async def setgr(message: types.Message, state: FSMContext):
    await state.update_data(group=message.text)
    grn = message.text
    us_id = message.from_user.id
    username = message.from_user.username
    s.db_table_main(user_id=us_id, username=username)
    if grn in grpi:
        print(grn)
        s.db_table_ed(grp=grn, user_id=us_id)
        await message.answer('Вы установили номер группы ' + grn, reply_markup=nav.mainMenu)
        await state.finish()
    else:
        await message.answer('Вы ввели не верный номер группы. \n' + 'Введите существующий номер группы.')
        await UserState.chgroup.set()


@dp.message_handler(commands=['chgroup'])
async def change_group(message: types.Message):
    await message.answer('Введите номер группы:\n')
    await UserState.chgroup.set()

@dp.message_handler(commands=['help'])
async def bot_messange(message: types.Message):
    await message.answer("🆘", reply_markup=nav.helpMenu)

@dp.message_handler(commands=['cmd'])
async def bot_messange(message: types.Message):
    await message.answer("/start \n/chgroup \n/cmd \n/help")





@dp.message_handler()
async def bot_messange(messange: types.Message):
    global num
    us_id = messange.from_user.id
    print(s.getName(conn=conn, user_id=us_id))
    grnum = int(s.getName(conn=conn, user_id=us_id))
    if messange.text == 'Выбор группы':
        await bot.send_message(messange.from_user.id, 'Введите номер своей группы', messange.text)
    elif messange.text == 'Замены🔄':
        await bot.send_message(messange.from_user.id, pr.zaminka(grnum))
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == '📋':
        await bot.send_message(messange.from_user.id, 'Выбери день мучений😩.', reply_markup=nav.otherMenu)
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == '⬅':
        await bot.send_message(messange.from_user.id, '⬅', reply_markup=nav.mainMenu)
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == '🔔':
        await bot.send_message(messange.from_user.id, pr.zvonki())
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Понедельник':
        await bot.send_message(messange.from_user.id, pr.ponedelnik(grnum))
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Вторник':
        await bot.send_message(messange.from_user.id, pr.vtornik(grnum))
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Среда':
        await bot.send_message(messange.from_user.id, pr.sreda(grnum))
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Четверг':
        await bot.send_message(messange.from_user.id, pr.chetverg(grnum))
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Пятница':
        await bot.send_message(messange.from_user.id, pr.pyatnica(grnum))
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Суббота':
        await bot.send_message(messange.from_user.id, pr.sybbota(grnum))
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Помощь🆘':
        await bot.send_message(messange.from_user.id, '🆘', reply_markup=nav.helpMenu)
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Команды':
        await bot.send_message(messange.from_user.id, '/start - Запуск бота(перезагрузка) \n/chgroup - Изменить группу \n/cmd - Список всех команд \n/help - Открывает меню "Помощь🆘"')
        await bot.delete_message(messange.from_user.id, messange.message_id)
    elif messange.text == 'Изменение группы':
        await bot.send_message(messange.from_user.id, 'Введите новый номер группы:\n')
        await UserState.chgroup.set()
    elif messange.text == 'Связь':
        await bot.send_message(messange.from_user.id,'Связь с нами:\nПо поводу своих предложений, идей пишите сюда:\n @Brat_satany'
                                                     '\nПо поводу тех. вопросов, нахождении багов пишите сюда:\n @kuzzz0\n'
                                                     '(всё исправим)\n'
                                                     'Будем рады вашей взаимности.❤')
        await bot.delete_message(messange.from_user.id, messange.message_id)
    else:
        await bot.send_message(messange.from_user.id, '', reply_markup=nav.mainMenu)

@dp.message_handler(state=UserState.chgroup)
async def change_gr(message: types.Message, state: FSMContext):
    await state.update_data(group=message.text)
    chgroup = message.text
    print(chgroup)
    us_id = message.from_user.id
    username = message.from_user.username
    if chgroup in grpi:
        s.db_table_ed(grp=chgroup, user_id=us_id)
        await message.answer('Вы установили номер группы ' + chgroup, reply_markup=nav.mainMenu)
        await state.finish()
    else:
        await message.answer('Вы ввели не верный номер группы. \n' + 'Введите существующий номер группы.')
        await UserState.chgroup()

async def on_startup():
    user_should_be_notified = 123123123123
    await bot.send_message(user_should_be_notified, 'Я снова работаю, ')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
