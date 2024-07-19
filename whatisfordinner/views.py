from django.shortcuts import render, get_object_or_404
from .models import Family, Member, FamilyAdmin, DinnerSuggestions

def family_list(request):
    families = Family.objects.all()
    return render(request, 'whatisfordinner/family_list.html', {'families': families})

def family_detail(request, family_id):
    family = get_object_or_404(Family, pk=family_id)
    return render(request, 'whatisfordinner/family_detail.html', {'family': family})

def member_list(request):
    members = Family.objects.all()
    return render(request, 'whatisfordinner/member_list.html', {'members': members})

def member_detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'whatisfordinner/member_detail.html', {'member': member})

def index(request):
    return render(request, 'whatisfordinner/index.html')