# Generated by Django 5.0.6 on 2024-07-19 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DinnerSuggestions",
            fields=[
                (
                    "dinner_suggestion_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("dinner_type", models.CharField(max_length=50)),
                ("date", models.DateField()),
                ("restaurant_or_meal_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="DeliveryOptions",
            fields=[
                (
                    "delivery_option_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("restaurant_name", models.CharField(max_length=50)),
                ("delivery_time", models.TimeField()),
                ("payment_opt", models.CharField(max_length=50)),
                ("cuisine_type", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Family",
            fields=[
                ("family_id", models.AutoField(primary_key=True, serialize=False)),
                ("family_name", models.CharField(max_length=50)),
                ("creation_date", models.DateField()),
                ("activity_status", models.CharField(max_length=50)),
                ("suggestion_deadline", models.TimeField()),
                ("dinner_deadline", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="HomeEntrees",
            fields=[
                ("meal_id", models.AutoField(primary_key=True, serialize=False)),
                ("meal_name", models.CharField(max_length=50)),
                ("ingredients", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                ("member_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                (
                    "family",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="whatisfordinner.family",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Restaurants",
            fields=[
                ("restaurant_id", models.AutoField(primary_key=True, serialize=False)),
                ("rest_name", models.CharField(max_length=50)),
                ("cuisine_type", models.CharField(max_length=50)),
                ("payment_options", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="FinalDiningChoices",
            fields=[
                (
                    "final_din_choice_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("date", models.DateField()),
                (
                    "dinner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="whatisfordinner.dinnersuggestions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FamilyAdmin",
            fields=[
                ("admin_id", models.AutoField(primary_key=True, serialize=False)),
                ("user_id", models.IntegerField()),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                (
                    "family",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="whatisfordinner.family",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="whatisfordinner.member",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="dinnersuggestions",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="whatisfordinner.member"
            ),
        ),
        migrations.CreateModel(
            name="Becomes",
            fields=[
                (
                    "final_din_choice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="whatisfordinner.finaldiningchoices",
                    ),
                ),
                (
                    "dinner_suggestion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="whatisfordinner.dinnersuggestions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CanBe",
            fields=[
                (
                    "dinner_suggestion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="whatisfordinner.dinnersuggestions",
                    ),
                ),
                (
                    "delivery_option",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="whatisfordinner.deliveryoptions",
                    ),
                ),
                (
                    "meal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="whatisfordinner.homeentrees",
                    ),
                ),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="whatisfordinner.restaurants",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Makes",
            fields=[
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="whatisfordinner.member",
                    ),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="whatisfordinner.familyadmin",
                    ),
                ),
                (
                    "dinner_suggestion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="whatisfordinner.dinnersuggestions",
                    ),
                ),
                (
                    "family",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="whatisfordinner.family",
                    ),
                ),
            ],
        ),
    ]
