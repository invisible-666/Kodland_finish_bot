# logik.py

from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Настройка базы данных
Base = declarative_base()
engine = create_engine('sqlite:///support_requests.db')  # Замените на DATABASE_URL из config.py
Session = sessionmaker(bind=engine)
session = Session()

class SupportRequest(Base):
    __tablename__ = 'support_requests'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    request_text = Column(Text)
    department = Column(String)

# Создание таблиц
Base.metadata.create_all(engine)

# Словарь для часто задаваемых вопросов
faq = {
    "Как оформить заказ?": "Для оформления заказа, пожалуйста, выберите интересующий вас товар и нажмите кнопку 'Добавить в корзину', затем перейдите в корзину и следуйте инструкциям для завершения покупки.",
    "Как узнать статус моего заказа?": "Вы можете узнать статус вашего заказа, войдя в свой аккаунт на нашем сайте и перейдя в раздел 'Мои заказы'.",
    "Как отменить заказ?": "Если вы хотите отменить заказ, пожалуйста, свяжитесь с нашей службой поддержки как можно скорее. Мы постараемся помочь вам с отменой заказа до его отправки.",
    "Что делать, если товар пришел поврежденным?": "При получении поврежденного товара, пожалуйста, сразу свяжитесь с нашей службой поддержки и предоставьте фотографии повреждений.",
    "Как связаться с вашей технической поддержкой?": "Вы можете связаться с нашей технической поддержкой через телефон на нашем сайте или написать нам в чат-бота.",
    "Как узнать информацию о доставке?": "Информацию о доставке вы можете найти на странице оформления заказа на нашем сайте. Там указаны доступные способы доставки и сроки."
}

def get_response(user_message):
    response = faq.get(user_message, "Извините, я не могу ответить на этот вопрос. Пожалуйста, свяжитесь с нашей поддержкой.")
    return response

def save_request(user_id, request_text):
    support_request = SupportRequest(user_id=user_id, request_text=request_text, department='Общий')
    session.add(support_request)
    session.commit()
