from django.contrib.auth.models import User

# Assuming you have a user's username
username = 'asdf'
new_password = 'put your new password here'

# Fetch the user
user = User.objects.get(username=username)

# Set the new password
user.set_password(new_password)
user.save()