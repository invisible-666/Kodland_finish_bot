# logik.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Update

# Данные для рекомендаций
career_data = {
    "технологии": "Программирование, веб-дизайн, IT-консалтинг.",
    "искусство": "Дизайн, музыка, живопись, актерское мастерство.",
    "наука": "Исследования, биология, физика, химия.",
    "бизнес": "Маркетинг, управление проектами, финансы."
}

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Получить рекомендации", callback_data='recommend')],
        [InlineKeyboardButton("Помощь", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Я Советчик по выбору карьеры. Чем могу помочь?', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'recommend':
        query.edit_message_text(text="Выберите вашу сферу интересов:",
                                 reply_markup=InlineKeyboardMarkup([
                                     [InlineKeyboardButton("Технологии", callback_data='технологии')],
                                     [InlineKeyboardButton("Искусство", callback_data='искусство')],
                                     [InlineKeyboardButton("Наука", callback_data='наука')],
                                     [InlineKeyboardButton("Бизнес", callback_data='бизнес')]
                                 ]))
    else:
        career_field = query.data
        recommendation = career_data.get(career_field, "Нет рекомендаций для этой сферы.")
        query.edit_message_text(text=f"Рекомендации для сферы '{career_field}': {recommendation}")
