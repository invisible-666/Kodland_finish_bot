import telebot
from config import TOKEN, DATABASE
from logik import SupportBotLogic

bot = telebot.TeleBot(TOKEN)
logic = SupportBotLogic(DATABASE)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в службу поддержки! Как я могу вам помочь?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    question = message.text
    response = logic.get_faq(question)

    bot.reply_to(message, response)

if __name__ == "__main__":
    bot.polling(none_stop=True)
