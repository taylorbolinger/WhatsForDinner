from django import forms
import datetime

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Family, Member, DinnerOptions, DinnerSuggestions

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
        

class DinnerSuggestionForm(forms.ModelForm):
    def __init__(self, family_id, member_id, date, *args, **kwargs):
        super(DinnerSuggestionForm, self).__init__(*args, **kwargs)
        self.fields['dinner_options_id'].queryset = DinnerOptions.objects.filter(
            family_id=family_id
        )  # this pulls back the options for the family_id, member_id
        # not DATE.  That is sent to Suggestions, not pulled from Options. duh.
        # not member b/c we are not filtering by member, we are filtering by family.
        
    class Meta:
        model = DinnerSuggestions
        fields = ['dinner_options_id']
        labels = {
            'dinner_options_id': 'Dinner Option'
        }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone_number']  # Correctly aligned with Member model

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput, help_text='Enter new password.')
    new_password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput, help_text='Enter new password again.')

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['family_name', 'suggestion_deadline', 'dinner_deadline']
        widgets = {
            'suggestion_deadline': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'dinner_deadline': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
        
class DinnerSuggestionFinalizationForm(forms.Form):
    suggestion = forms.ModelChoiceField(
        queryset=DinnerSuggestions.objects.none(),
        widget=forms.RadioSelect,
        empty_label=None
    )

    def __init__(self, *args, **kwargs):
        member = kwargs.pop('member', None)
        super().__init__(*args, **kwargs)
        if member and member.family_id:
            today = datetime.date.today()
            self.fields['suggestion'].queryset = DinnerSuggestions.objects.filter(
                family_id=member.family_id, date=today
            )