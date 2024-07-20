from whatisfordinner.models import Member
from django.utils.crypto import get_random_string

# Sample data for 15 members
members_data = [
    {"name": "John Doe", "email": "john.doe@example.com", "phone_number": "1234567890"},
    {"name": "Jane Smith", "email": "jane.smith@example.com", "phone_number": "0987654321"},
    {"name": "Alice Johnson", "email": "alice.johnson@example.com", "phone_number": "2345678901"},
    {"name": "Bob Brown", "email": "bob.brown@example.com", "phone_number": "3456789012"},
    {"name": "Charlie Davis", "email": "charlie.davis@example.com", "phone_number": "4567890123"},
    {"name": "Diana Evans", "email": "diana.evans@example.com", "phone_number": "5678901234"},
    {"name": "Eve Foster", "email": "eve.foster@example.com", "phone_number": "6789012345"},
    {"name": "Frank Green", "email": "frank.green@example.com", "phone_number": "7890123456"},
    {"name": "Grace Harris", "email": "grace.harris@example.com", "phone_number": "8901234567"},
    {"name": "Hank Ingram", "email": "hank.ingram@example.com", "phone_number": "9012345678"},
    {"name": "Ivy Jackson", "email": "ivy.jackson@example.com", "phone_number": "0123456789"},
    {"name": "Jack King", "email": "jack.king@example.com", "phone_number": "1234509876"},
    {"name": "Karen Lee", "email": "karen.lee@example.com", "phone_number": "2345609876"},
    {"name": "Leo Martin", "email": "leo.martin@example.com", "phone_number": "3456709876"},
    {"name": "Mona Nelson", "email": "mona.nelson@example.com", "phone_number": "4567809876"},
]

# Create and save members
for member_data in members_data:
    member = Member(**member_data)
    member.save()

print("15 members have been added.")