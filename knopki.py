from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('⬅')
#Главные кнокпи
btnZam = KeyboardButton ('Замены🔄')
btnRasp = KeyboardButton('📋')
btnZvon = KeyboardButton('🔔')
btnhelp = KeyboardButton("Помощь🆘")
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.row(btnZam, btnRasp, btnZvon).add(btnhelp)
#btngroup =KeyboardButton("Выбор группы")

#Второстепенные кнопки
btnPn = KeyboardButton('Понедельник')
btnVt = KeyboardButton('Вторник')
btnSr = KeyboardButton('Среда')
btnCht = KeyboardButton('Четверг')
btnPt = KeyboardButton('Пятница')
btnSb = KeyboardButton('Суббота')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnPn, btnVt, btnSr, btnCht, btnPt, btnSb, btnMain)
btnCmd = KeyboardButton("Команды")
btngroup = KeyboardButton("Изменение группы")
btncall = KeyboardButton("Связь")
helpMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btncall, btnCmd, btngroup).row(btnMain)
