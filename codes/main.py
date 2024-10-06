# main.py

import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TELEGRAM_BOT_TOKEN
from logik import get_response, save_request

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот поддержки. Чем могу помочь?')

# Функция для обработки текстовых сообщений
def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.strip()
    response = get_response(user_message)

    # Сохранение запроса в базу данных
    save_request(update.message.from_user.id, user_message)

    update.message.reply_text(response)

# Основная функция
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Регистрация обработчиков
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
