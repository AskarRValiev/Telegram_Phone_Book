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
        context.bot.send_message(update.effective_chat.id, controller.phonebook)
    else:
        context.bot.send_message(update.effective_chat.id, "Не понял сейчас")


def add(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Вносим новый контакт в справочник, вводи id, фамилию, имя, отчество, телефон\
        в формате +7-***-***-**-** и комментарий")
        status.insert(0, 'cont_adding')
    else:
        context.bot.send_message(update.effective_chat.id, "Не понял сейчас")

def delete(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Введи ФИО удаляемого контакта:")
        status.insert(0, 'del_cont')
    else:
        context.bot.send_message(update.effective_chat.id, "Не понял сейчас")


def message(update, context):
    text = update.message.text
    #print(status)
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'Привет! Я работаю с телефонным справочником. Для работы используй команды:\
        \n/contacts - просмотр контактов\n/add - добавление контакта\n/delete - удаление контакта\n/change - изменение контакта')
    elif text.lower() != 'привет' and status != []: #[0] == 'cont_adding':
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
            if res == '1':
                context.bot.send_message(update.effective_chat.id, 'Контакт деактивирован.')
            else:
                context.bot.send_message(update.effective_chat.id, 'Контакт не найден.')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')
        




contacts_handler = CommandHandler('contacts', contacts)#/contacts вывод контактов
add_handler = CommandHandler('add', add)#/add добавление контакта
del_handler = CommandHandler('delete', delete)#/add добавлен4ие контакта
message_handler = MessageHandler(Filters.text, message)



dispatcher.add_handler(contacts_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(del_handler)
dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()