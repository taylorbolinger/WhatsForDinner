from django.db import models

# Create your models here.

class Family(models.Model):
    family_id = models.AutoField(primary_key=True)
    family_name = models.CharField(max_length=50)
    creation_date = models.DateField()
    activity_status = models.CharField(max_length=50)
    suggestion_deadline = models.TimeField()
    dinner_deadline = models.TimeField()

    def __str__(self):
        return self.family_name


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FamilyAdmin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DinnerSuggestions(models.Model):
    dinner_suggestion_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    dinner_type = models.CharField(max_length=50)
    date = models.DateField()
    restaurant_or_meal_name = models.CharField(max_length=50)

    def __str__(self):
        return self.restaurant_or_meal_name


class FinalDiningChoices(models.Model):
    final_din_choice_id = models.AutoField(primary_key=True)
    dinner = models.ForeignKey(DinnerSuggestions, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"Final Choice on {self.date}"


class HomeEntrees(models.Model):
    meal_id = models.AutoField(primary_key=True)
    meal_name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=50)

    def __str__(self):
        return self.meal_name


class Restaurants(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    rest_name = models.CharField(max_length=50)
    cuisine_type = models.CharField(max_length=50)
    payment_options = models.CharField(max_length=50)

    def __str__(self):
        return self.rest_name


class DeliveryOptions(models.Model):
    delivery_option_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=50)
    delivery_time = models.TimeField()
    payment_opt = models.CharField(max_length=50)
    cuisine_type = models.CharField(max_length=50)

    def __str__(self):
        return self.restaurant_name


class Makes(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, primary_key=True)
    dinner_suggestion = models.ForeignKey(DinnerSuggestions, on_delete=models.CASCADE)
    admin = models.ForeignKey(FamilyAdmin, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return f"Made by {self.member}"


class CanBe(models.Model):
    dinner_suggestion = models.ForeignKey(DinnerSuggestions, on_delete=models.CASCADE, primary_key=True)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    meal = models.ForeignKey(HomeEntrees, on_delete=models.CASCADE)
    delivery_option = models.ForeignKey(DeliveryOptions, on_delete=models.CASCADE)

    def __str__(self):
        return f"Can be {self.restaurant} or {self.meal}"


class Becomes(models.Model):
    final_din_choice = models.ForeignKey(FinalDiningChoices, on_delete=models.CASCADE, primary_key=True)
    dinner_suggestion = models.ForeignKey(DinnerSuggestions, on_delete=models.CASCADE)

    def __str__(self):
        return f"Becomes {self.final_din_choice}"