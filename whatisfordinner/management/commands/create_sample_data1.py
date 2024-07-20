from django.core.management.base import BaseCommand
from whatisfordinner.models import Family, Member, FamilyAdmin, DinnerSuggestions, FinalDiningChoices, HomeEntrees, Restaurants, DeliveryOptions
from datetime import date, time

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Create Family instances
        family1 = Family.objects.create(
            family_name='Smith',
            creation_date=date(2023, 1, 1),
            activity_status='Active',
            suggestion_deadline=time(18, 0),
            dinner_deadline=time(20, 0)
        )

        family2 = Family.objects.create(
            family_name='Johnson',
            creation_date=date(2023, 2, 1),
            activity_status='Inactive',
            suggestion_deadline=time(19, 0),
            dinner_deadline=time(21, 0)
        )

        # Create Member instances
        member1 = Member.objects.create(
            family=family1,
            first_name='John',
            last_name='Smith',
            email='john.smith@example.com'
        )

        member2 = Member.objects.create(
            family=family1,
            first_name='Jane',
            last_name='Smith',
            email='jane.smith@example.com'
        )

        member3 = Member.objects.create(
            family=family2,
            first_name='Alice',
            last_name='Johnson',
            email='alice.johnson@example.com'
        )

        # Create FamilyAdmin instances
        admin1 = FamilyAdmin.objects.create(
            user_id=1,
            member=member1,
            family=family1,
            first_name='John',
            last_name='Smith',
            email='john.smith@example.com'
        )

        admin2 = FamilyAdmin.objects.create(
            user_id=2,
            member=member3,
            family=family2,
            first_name='Alice',
            last_name='Johnson',
            email='alice.johnson@example.com'
        )

        # Create DinnerSuggestions instances
        suggestion1 = DinnerSuggestions.objects.create(
            member=member1,
            dinner_type='Home-cooked',
            date=date(2023, 3, 1),
            restaurant_or_meal_name='Spaghetti Bolognese'
        )

        suggestion2 = DinnerSuggestions.objects.create(
            member=member2,
            dinner_type='Restaurant',
            date=date(2023, 3, 2),
            restaurant_or_meal_name='Pizza Place'
        )

        # Create FinalDiningChoices instances
        final_choice1 = FinalDiningChoices.objects.create(
            dinner=suggestion1,
            date=date(2023, 3, 1)
        )

        final_choice2 = FinalDiningChoices.objects.create(
            dinner=suggestion2,
            date=date(2023, 3, 2)
        )

        # Create HomeEntrees instances
        entree1 = HomeEntrees.objects.create(
            meal_name='Spaghetti Bolognese',
            ingredients='Spaghetti, Beef, Tomato Sauce'
        )

        entree2 = HomeEntrees.objects.create(
            meal_name='Chicken Alfredo',
            ingredients='Chicken, Alfredo Sauce, Pasta'
        )

        # Create Restaurants instances
        restaurant1 = Restaurants.objects.create(
            rest_name='Pizza Place',
            cuisine_type='Italian',
            payment_options='Credit Card, Cash'
        )

        restaurant2 = Restaurants.objects.create(
            rest_name='Sushi World',
            cuisine_type='Japanese',
            payment_options='Credit Card, Cash, PayPal'
        )

        # Create DeliveryOptions instances
        delivery_option1 = DeliveryOptions.objects.create(
            restaurant_name='Pizza Place',
            delivery_time=time(19, 0),
            payment_opt='Credit Card'
        )

        delivery_option2 = DeliveryOptions.objects.create(
            restaurant_name='Sushi World',
            delivery_time=time(20, 0),
            payment_opt='PayPal'
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))