# Django standard library imports
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone

# Authentication related imports
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Local application imports
from .forms import SignUpForm, DinnerOptionsForm, DinnerSuggestionForm
from .models import Member, DinnerOptions, DinnerSuggestions

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
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
        family_id = user_member.family_id.family_id  # Assuming this is how you get the family_id
    except (AttributeError, Member.DoesNotExist):
        # Handle cases where the user does not have a family or member profile
        return HttpResponse("You must be a member of a family to view this page.")
    
    # Initialize context dictionary
    context = {}

    # Get dinner suggestions for the user's family for today
    today = timezone.now().date()
    dinner_suggestions = DinnerSuggestions.objects.filter(family_id=family_id, date=today)

    # Check if there are any dinner suggestions for today
    if dinner_suggestions.exists():
        # Display the dinner suggestions for today
        context['dinner_suggestions'] = dinner_suggestions

    # Handle form submission
    if request.method == 'POST':
        form = DinnerSuggestionForm(request.POST, family_id=family_id)
        if form.is_valid():
            dinner_suggestion = form.save(commit=False)
            dinner_suggestion.family_id = family_id
            dinner_suggestion.save()
            return redirect('dinner_suggestion_view')
    else:
        form = DinnerSuggestionForm(family_id=family_id)

    context['form'] = form
    return render(request, 'dinner-suggestions.html', context)

# t-shootin fun getting django toolbar going: 
def show_client_ip_view(request):
    client_ip = request.META.get('REMOTE_ADDR', None)
    return HttpResponse(f"Your IP Address is: {client_ip}") ## shows loopback via docker