from pkg.find_face import FindFace
from pkg.image import merge_images
from pkg.tg_bot import TgBot
from webhook.models import Event, User


def create_notification(webhook):
    original = FindFace().get_original_photo(card_id=webhook['matched_card']['id'])
    thumbnail = merge_images(original, webhook['last_face_event']['thumbnail'])
    event = Event.objects.create(
        name=webhook['matched_card']['name'],
        full_frame=webhook['last_face_event']['fullframe'],
        thumbnail=thumbnail,
    )
    message_text = f'дата: {event.date}\nПерсонаж: {event.name}'
    keyboard = {
        'text': 'Показать фото с камеры',
        'data': f'origin:{event.id}'
    }
    for user in User.objects.filter(send_notification=True):
        TgBot().send_message(user.tg_chat_id, text=message_text, keyboard_data=keyboard, photo=event.thumbnail)