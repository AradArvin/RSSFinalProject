from django.core.management.base import BaseCommand
from accounts.consumers import *



class Command(BaseCommand):
    help = 'Start massage consumers'

    def handle(self, *args, **options):
        
        queues = ["login", "register", "UpdateRss", "ParseRss"]
        
        for queue in queues:
            consumer_starter(queue=queue)
        
        self.stdout("Consumers are running...")