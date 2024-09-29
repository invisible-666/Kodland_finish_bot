# Библиотеки
import logging
import sqlite3
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Подключение к базе данных SQLite
conn = sqlite3.connect('requests.db')
cursor = conn.cursor()

# Создание таблицы для хранения запросов
cursor.execute('''
CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    query TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)''')
conn.commit()

# Словарь с FAQ
faq = {
    "Как оформить заказ?",
    "Для оформления заказа, пожалуйста, выберите интересующий вас товар и нажмите кнопку 'Добавить в корзину', затем перейдите в корзину и следуйте инструкциям для завершения покупки.",
    "Как узнать статус моего заказа?"
    "Вы можете узнать статус вашего заказа, войдя в свой аккаунт на нашем сайте и перейдя в раздел 'Мои заказы'. Там будет указан текущий статус вашего заказа.",
    "Как отменить заказ?",
    "Если вы хотите отменить заказ, пожалуйста, свяжитесь с нашей службой поддержки как можно скорее. Мы постараемся помочь вам с отменой заказа до его отправки.",
    "Что делать, если товар пришел поврежденным?",
    "При получении поврежденного товара, пожалуйста, сразу свяжитесь с нашей службой поддержки и предоставьте фотографии повреждений. Мы поможем вам с обменом или возвратом товара.",
    "Как связаться с вашей технической поддержкой?",
    "Вы можете связаться с нашей технической поддержкой через телефон на нашем сайте или написать нам в чат-бота.",
    "Как узнать информацию о доставке?",
    "Информацию о доставке вы можете найти на странице оформления заказа на нашем сайте. Там указаны доступные способы доставки и сроки."
}

# Команда /start
def start(update: Update, context: CallbackContext):
    """Отправляет приветственное сообщение."""
    update.message.reply_text('Добро пожаловать! Введите ваш вопрос или используйте команды.')

# Обработка текстовых сообщений
def handle_message(update: Update, context: CallbackContext):
    """Обрабатывает текстовые сообщения от пользователей."""
    user_message = update.message.text

    # Проверка на наличие вопроса в FAQ
    if user_message in faq:
        update.message.reply_text(faq[user_message])
    else:
        # Сохранение запроса в БД
        cursor.execute("INSERT INTO requests (user_id, query) VALUES (?, ?)", (update.message.from_user.id, user_message))
        conn.commit()
        update.message.reply_text('Ваш запрос сохранен! Мы ответим вам в ближайшее время.')

# Команда /help
def help_command(update: Update, context: CallbackContext):
    """Отправляет информацию о командах."""
    update.message.reply_text('Доступные команды:\n/start - Начать общение с ботом\n/help - Помощь по командам')

# Основная функция
def main():
    """Запуск бота."""
    # Создаем Updater и передаем токен бота
    updater = Updater("7500676368:AAGgdXUt4weQuwEeifCG7Qi13F1w368J5Dk", use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрация обработчиков
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()

# Проверка на запуск скрипта
if __name__ == '__main__':
    main()