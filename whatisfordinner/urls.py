from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('families/', views.family_list, name='family_list'),
    path('families/<int:family_id>/', views.family_detail, name='family_detail'),
    path('members/', views.member_list, name='member_list'),
    path('members/<int:member_id>/', views.member_detail, name='member_detail'),
    path('', index, name='index'),

]