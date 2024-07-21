from django.core.management.base import BaseCommand
from whatisfordinner.models import Member  

class Command(BaseCommand):
    help = 'Lists all members'

    def handle(self, *args, **kwargs):
        members = Member.objects.all()
        for member in members:
            self.stdout.write(f'{member.user.username} - {member.family_id}- {member.email}: {member.name} - {member.email} ')
            
# usage - python manage.py list_members
