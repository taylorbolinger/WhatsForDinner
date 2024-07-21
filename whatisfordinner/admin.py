from django.contrib import admin
from .models import Member

## this add stuff to the admin page. 
# Register your models here.
admin.site.register(Member)