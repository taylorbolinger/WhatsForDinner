from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Family, Member, DinnerOptions

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address.')
    phone_number = forms.CharField(max_length=15, required=False)
    family_id = forms.ModelChoiceField(queryset=Family.objects.all(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'name', 'phone_number', 'family_id')
        

class DinnerOptionsForm(forms.ModelForm):
    class Meta:
        model = DinnerOptions
        fields = ['name', 'ingredients', 'cuisine_type', 'entry_type']