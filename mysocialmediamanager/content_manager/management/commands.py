
from django.core.management.base import BaseCommand
from content_manager.agents import run_agents

class Command(BaseCommand):
    help = 'Runs the content posting agents'

    def handle(self, *args, **options):
        run_agents()
        self.stdout.write(self.style.SUCCESS('Successfully ran agents'))
