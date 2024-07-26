import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

# Create your models here.

class Family(models.Model):
    family_id = models.AutoField(primary_key=True)
    family_name = models.CharField(max_length=50)
    admin_member_id = models.ForeignKey('Member', on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateField(default=datetime.date.today)
    suggestion_deadline = models.TimeField(default='14:00')
    dinner_deadline = models.TimeField(default='17:00')
  
    def __str__(self):
        return self.family_name

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='member_profile')
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    
    
    def __str__(self):
        return self.name


class DinnerSuggestions(models.Model):
    dinner_suggestion_id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    family_id = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, blank=True)
    dinner_options_id = models.ForeignKey('DinnerOptions', on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    is_final_choice = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member_id.name} suggested {self.dinner_options_id.name} for {self.date.strftime('%m/%d/%Y')}"

class DinnerOptions(models.Model):
    dinner_options_id = models.AutoField(primary_key=True)
    family_id = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=50, null=True, blank=True)
    cuisine_type_choices = [
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('chinese', 'Chinese'),
        ('indian', 'Indian'),
        ('japanese', 'Japanese'),
        ('american', 'American'),
        ('french', 'French'),
        ('mediterranean', 'Mediterranean'),
        ('thai', 'Thai'),
        ('greek', 'Greek'),
    ]
    cuisine_type = models.CharField(max_length=50, null=True, blank=True, choices=cuisine_type_choices)
    ENTRY_TYPE_CHOICES = [
        ('home_entree', 'Home Entree'),
        ('restaurant', 'Restaurant'),
        ('delivery_option', 'Delivery Option'),
    ]
    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.family_id.family_name}) - {self.entry_type} ({self.cuisine_type})"
