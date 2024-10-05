# main.py
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from config import TOKEN
from logik import start, button

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, lambda update, context: update.message.reply_text("Пожалуйста, используйте меню.")))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
