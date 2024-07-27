# Django standard library imports
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.forms import PasswordChangeForm
import datetime

# Authentication related imports
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Local application imports
from .forms import SignUpForm, DinnerOptionsForm, DinnerSuggestionForm, MemberForm, CustomPasswordChangeForm, FamilyForm, DinnerSuggestionFinalizationForm
from .models import Member, DinnerOptions, DinnerSuggestions, Family 


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            member = Member.objects.create(
                user=user,
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                phone_number=form.cleaned_data.get('phone_number'),
                family_id=form.cleaned_data.get('family_id')
            )
            login(request, user)
            return redirect('index')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
        

def logout_view(request):
    logout(request)
    return redirect('index')  

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to a success page.
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user
    member, created = Member.objects.get_or_create(user=user)

    if request.method == 'POST':
        # Handle the password change form
        if 'password_change' in request.POST:
            password_form = CustomPasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Keep the user logged in
                return redirect('profile')
        else:
            # Handle the member form
            member_form = MemberForm(request.POST, instance=member)
            if member_form.is_valid():
                member_form.save()
                return redirect('profile')
    else:
        # Instantiate forms
        password_form = CustomPasswordChangeForm(user)
        member_form = MemberForm(instance=member)
    
    context = {
        'password_form': password_form,
        'member_form': member_form
    }
    return render(request, 'userprofile.html', context)

@login_required
def dinner_options_view(request):
    # Get the current user's family
    try:
        family = request.user.member.family_id
    except AttributeError:
        # Handle cases where the user does not have a family or member profile
        return HttpResponse("You must be a member of a family to view this page.")

    # Handle form submission
    if request.method == 'POST':
        form = DinnerOptionsForm(request.POST)
        if form.is_valid():
            dinner_option = form.save(commit=False)
            dinner_option.family_id = family
            dinner_option.save()
            return redirect('dinner_options_view')
    else:
        form = DinnerOptionsForm()

    # Get dinner options for the user's family
    dinner_options = DinnerOptions.objects.filter(family_id=family)

    return render(request, 'dinner-options.html', {'dinner_options': dinner_options, 'form': form})


## not working yet.
@login_required
def dinner_suggestion_view(request):
    try:
        user_member = Member.objects.get(user=request.user)  
        family = user_member.family_id  # Get the Family instance
    except (AttributeError, Member.DoesNotExist):
        # Handle cases where the user does not have a family or member profile
        return HttpResponse("You must be a member of a family to view this page.")

    context = {} # Initialize context dictionary

    # Get dinner suggestions for the user's family for today
    today = timezone.now().date()
    users_dinner_suggestions = DinnerSuggestions.objects.filter(member_id=user_member.member_id, date=today) # this needs to be filtered by the mmeber, not the family.  duh.

    # Check if there are any dinner suggestions for today by this user.
    if users_dinner_suggestions.exists():
        # Display the dinner suggestions for today
        ## not giving the option to make another suggestion
        context['users_dinner_suggestions'] = users_dinner_suggestions
        first = users_dinner_suggestions.first() # there will always only be 1 suggestion per user per day.
        context['users_dinner_suggestions_message'] = f"{first.member_id.name} suggested {first.dinner_options_id.name} for {first.date.strftime('%m/%d/%Y')}"
        context['message'] = "You have already made a dinner suggestion for today."
        return render(request, 'dinner-suggestions.html', context)

    # Handle form submission
    # specific to family, member, and date!
    if request.method == 'POST':
        form = DinnerSuggestionForm(data=request.POST, family_id=family.family_id, member_id=user_member.member_id, date=today)
        if form.is_valid():
            dinner_suggestion = form.save(commit=False)
            dinner_suggestion.family_id = family  # Assign the Family instance
            dinner_suggestion.member_id = user_member  # Assign the Member instance
            dinner_suggestion.date = timezone.now().date() # default in model?  
            dinner_suggestion.save()
            return redirect('dinner_suggestion_view')
    else:
        form = DinnerSuggestionForm(family_id=family.family_id, member_id=user_member.member_id, date=today)

    context['form'] = form
    return render(request, 'dinner-suggestions.html', context)

# t-shootin fun getting django toolbar going: 
def show_client_ip_view(request):
    client_ip = request.META.get('REMOTE_ADDR', None)
    return HttpResponse(f"Your IP Address is: {client_ip}") ## shows loopback via docker

def create_family(request):
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            family = form.save(commit=False)
            family.creation_date = timezone.now().date()
            family.admin_member_id = request.user.member
            family.save()
            return redirect('index')  # Redirect to the desired page after successful form submission
    else:
        form = FamilyForm()
    return render(request, 'create_family.html', {'form': form})

@login_required
def dinner_decision_view(request):
    user = request.user
    try:
        member = Member.objects.get(user=user)
        is_admin = Family.objects.filter(admin_member_id=member).exists()
    except Member.DoesNotExist:
        member = None
        is_admin = False

    today = datetime.date.today()
    final_choice = DinnerSuggestions.objects.filter(family_id=member.family_id, date=today, is_final_choice=True).first()
    final_dinner_option = final_choice.dinner_options_id if final_choice else None

    member_final_choice_maker = final_choice.member_id if final_choice else None

    if request.method == 'POST' and is_admin:
        form = DinnerSuggestionFinalizationForm(request.POST, member=member)
        if form.is_valid():
            suggestion = form.cleaned_data['suggestion']
            suggestion.is_final_choice = True
            suggestion.save()
            return redirect('dinner_decision')
    else:
        form = DinnerSuggestionFinalizationForm(member=member)

    context = {
        'is_admin': is_admin,
        'member': member,
        'form': form,
        'final_choice': final_choice,
        'final_choice_maker': member_final_choice_maker,
        'final_dinner_option': final_dinner_option,
        'current_date': today,
        
    }
    return render(request, 'dinner-decision.html', context)

def create_family(request):
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            family = form.save(commit=False)
            if request.user.is_authenticated:
                try:
                    family.admin_member_id = request.user.member
                except Member.DoesNotExist:
                    raise Http404("Authenticated user has no member profile")
            else:
                family.admin_member_id = None  # or set to a default value if needed
            family.save()
            return redirect('index')  # Redirect to the family details page or any other appropriate page
    else:
        form = FamilyForm()
    return render(request, 'create_family.html', {'form': form})