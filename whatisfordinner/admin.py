from django.contrib import admin
from .models import Member, Family, DinnerOptions, DinnerSuggestions

# Register your models here.
admin.site.register(Member)
admin.site.register(Family)
admin.site.register(DinnerOptions)
admin.site.register(DinnerSuggestions)
