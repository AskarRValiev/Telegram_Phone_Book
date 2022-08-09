from queue import Empty
from turtle import update
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN
import controller
import change

status = []


bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
    

def contacts(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, controller.phonebook )
    else:
        context.bot.send_message(update.effective_chat.id, "Не понял сейчас")


def add(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Вносим новый контакт в справочник, вводи id, фамилию, имя, отчество, телефон\
        в формате +7-XXX-XXX-XX-XX и комментарий(можно забить если память хорошая)")
        status.insert(0, 'cont_adding')
    else:
        context.bot.send_message(update.effective_chat.id, "Не понял сейчас")

def delete(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Введи данные удаляемого контакта, можно несколько букв или цифр, я умный)):")
        status.insert(0, 'del_cont')
    else:
        context.bot.send_message(update.effective_chat.id, "Не понял сейчас")

def change_cont(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Введи данные изменяемого контакта, можно несколько букв:")
        status.insert(0, 'chng_cont')
    else:
        context.bot.send_message(update.effective_chat.id, "Не понял сейчас")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'Привет! Я работаю с телефонным справочником. Для работы используй команды:\
        \n/contacts - просмотр контактов\n/add - добавление контакта\n/delete - удаление контакта\n/change - изменение контакта')
    elif text.lower() != 'привет' and status != []:
        if status[0] == 'cont_adding':
            res = change.write_data_one_string(text)
            if res == '1':
                context.bot.send_message(update.effective_chat.id, "Контакт внесён.")
            elif res == 'to_id':
                context.bot.send_message(update.effective_chat.id, "Такой ID уже есть, попробуй снова.")
            elif res == 'to_number':
                context.bot.send_message(update.effective_chat.id, "Такой номер уже есть, ты забыл.")
            else:
                context.bot.send_message(update.effective_chat.id, "Ошибка! Проверь вводимые данные!")
            status.clear()
        elif status[0] == 'del_cont':
            res = change.delete_contact(text)
            if res == '':
                context.bot.send_message(update.effective_chat.id, 'Контакт не найден')
            else:
                context.bot.send_message(update.effective_chat.id, f'Найдены контакты:\n {res}')
                context.bot.send_message(update.effective_chat.id, 'Введи ID кого будем удалять:')
                status[0] = 'del_id'
        elif status[0] == 'del_id':
            res = change.delete_id(text)
            if res == '1':
                context.bot.send_message(update.effective_chat.id, 'Контакт удален')
            else:
                context.bot.send_message(update.effective_chat.id, 'Контакт не найден')
            status.clear()
        elif status[0] == 'chng_cont':
            res = change.delete_contact(text)
            if res == '':
                print(res)
                context.bot.send_message(update.effective_chat.id, 'Контакт не найден')
            else:
                context.bot.send_message(update.effective_chat.id, f'Найдены контакты:\n {res}')
                context.bot.send_message(update.effective_chat.id, 'Введи через пробел: ID кого будем менять, что будем менять, \
                    на что будем менять (что то одно: фамилия, имя, отчество, телефон):')
                status[0] = 'chng_id'
        elif status[0] == 'chng_id':
            res = change.chng_id(text)
            if res == '1':
                context.bot.send_message(update.effective_chat.id, 'Контакт изменен')
            else:
                context.bot.send_message(update.effective_chat.id, 'Контакт не найден')
            status.clear()

    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')
        




contacts_handler = CommandHandler('contacts', contacts)#/contacts вывод контактов
add_handler = CommandHandler('add', add)#/add добавление контакта
del_handler = CommandHandler('delete', delete)#/delete удаление контакта
chng_handler = CommandHandler('change', change_cont)#/delete удаление контакта
message_handler = MessageHandler(Filters.text, message)



dispatcher.add_handler(contacts_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(del_handler)
dispatcher.add_handler(chng_handler)
dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()