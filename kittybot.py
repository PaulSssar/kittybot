# from telegram import Bot
# from telegram.ext import Updater
# bot = Bot(token='5844108449:AAEqL6Fwt0VVuajZtOnXltGRtd67tdkZFT8')
# updater = Updater(token='5844108449:AAEqL6Fwt0VVuajZtOnXltGRtd67tdkZFT8')
# chat = 1151845150
# bot.send_message(chat, 'прив')
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup

updater = Updater(token='5844108449:AAEqL6Fwt0VVuajZtOnXltGRtd67tdkZFT8')


def say_hello(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! I'm KittyBot")


def wake_up(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['Показать фото котика']])
    context.bot.send_message(chat_id=chat.id, text=f"I'm wake up, {chat.first_name}!", reply_markup=button)

updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hello))


updater.start_polling()
updater.idle()