from django.core.management.base import BaseCommand
from accounts.consumers import *



class Command(BaseCommand):
    help = 'Start massage consumers'

    def handle(self, *args, **options):
        login_consumer()
        register_consumer()
        rss_update_consumer()
        rss_parser_consumer