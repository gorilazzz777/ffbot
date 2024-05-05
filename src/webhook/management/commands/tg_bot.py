from django.core.management import BaseCommand

from pkg.tg_bot import TgBot


class Command(BaseCommand):
    help = 'Запуск ТГ бота'

    def handle(self, *args, **kwargs) -> None:
        TgBot().start_pooling()