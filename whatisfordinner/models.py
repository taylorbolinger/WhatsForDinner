## this is a sample and does not fit the currernt data model
import datetime
from django.db import models

# Create your models here.

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    family_id = models.ForeignKey('Family', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class Family(models.Model):
    family_id = models.AutoField(primary_key=True)
    family_name = models.CharField(max_length=50)
    creation_date = models.DateField(default=datetime.date.today)
    admin_member_id = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    suggestion_deadline = models.TimeField(default='14:00')
    dinner_deadline = models.TimeField(default='17:00')
    
    def __str__(self):
        return self.family_name

class DinnerSuggestions(models.Model):
    dinner_suggestion_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    family_id = models.ForeignKey(Family, on_delete=models.CASCADE)
    dinner_options_id = models.ForeignKey('DinnerOptions', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    is_final_choice = models.BooleanField(default=False)

    def __str__(self):
        if self.is_final_choice:
            return f"Final Choice on {self.date}"
        return self.restaurant_or_meal_name

class DinnerOptions(models.Model):
    dinner_options_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=50, null=True, blank=True)
    cuisine_type = models.CharField(max_length=50, null=True, blank=True)
    payment_options = models.CharField(max_length=50, null=True, blank=True)
    delivery_time = models.TimeField(null=True, blank=True)
    ENTRY_TYPE_CHOICES = [
        ('home_entree', 'Home Entree'),
        ('restaurant', 'Restaurant'),
        ('delivery_option', 'Delivery Option'),
    ]
    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPE_CHOICES)

    def __str__(self):
        return self.name

    