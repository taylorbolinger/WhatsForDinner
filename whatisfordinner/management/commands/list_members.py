from django.core.management.base import BaseCommand
from whatisfordinner.models import Member  

class Command(BaseCommand):
    help = 'Lists all members'

    def handle(self, *args, **kwargs):
        members = Member.objects.all()
        for member in members:
            self.stdout.write(f'{member.id}: {member.name} - {member.email}')