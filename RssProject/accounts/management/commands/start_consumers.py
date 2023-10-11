from django.core.management.base import BaseCommand
from accounts.consumers import login_consumer, register_consumer, rss_consumer



class Command(BaseCommand):
    help = 'Start massage consumers'

    def handle(self, *args, **options):
        login_consumer()
        register_consumer()