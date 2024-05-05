import os

import telebot
from telebot import types

bot = telebot.TeleBot(os.getenv('TG_TOKEN', '7183801317:AAHWE2ww6y3F7rZY5zmNu93xeLuiL-gwRR4'))


class TgBot:
    def send_message(self, chat_id, text, photo, keyboard_data: dict):
        keyboard = types.InlineKeyboardMarkup()
        key = types.InlineKeyboardButton(text=keyboard_data['text'], callback_data=keyboard_data['data'])
        keyboard.add(key)
        bot.send_photo(chat_id=chat_id, photo=open(photo.name, 'rb'), caption=text, reply_markup=keyboard)

    def delete_message(self, chat_id, message_id):
        bot.delete_message(chat_id=chat_id, message_id=message_id)

    def start_pooling(self):
        while True:
            try:
                bot.polling(none_stop=True, interval=0)
            except:
                pass


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    from webhook.models import Event

    type_photo, event_id = call.data.split(':')
    event = Event.objects.get(id=event_id)
    message_text = f'дата: {event.date}\nПерсонаж: {event.name}'
    keyboard = {
        'text': 'Full Photo',
        'data': f'origin:{event.id}'
    }
    if type_photo == "origin":
        keyboard = {
            'text': 'Показать превью',
            'data': f'trumb:{event.id}'
        }
        photo = event.full_frame
    else:
        keyboard = {
            'text': 'Показать фото с камеры',
            'data': f'origin:{event.id}'
        }
        photo = event.thumbnail
    TgBot().send_message(call.message.chat.id, text=message_text, photo=photo, keyboard_data=keyboard)
    TgBot().delete_message(call.message.chat.id, call.message.id)