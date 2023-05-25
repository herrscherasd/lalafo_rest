from typing import Any, Optional
from django.core.management.base import BaseCommand
from apps.telegram.views import dp, executor


class Command(BaseCommand):
    help = 'Start Bot Aiogram'

    def handle(self, *args: Any, **options: Any) -> str | None:
        print('Start Bot')
        executor.start_polling(dp, skip_updates=True)