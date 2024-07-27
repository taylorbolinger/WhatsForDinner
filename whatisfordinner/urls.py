from django.urls import path
from . import views
from .views import signup_view, logout_view, user_login, dinner_options_view, dinner_suggestion_view, show_client_ip_view

urlpatterns = [
    path('', views.index, name='index'),  
    path('index/', views.index, name='index'),  
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('dinner-options/', views.dinner_options_view, name='dinner_options_view'),
    path('dinner-suggestions/', views.dinner_suggestion_view, name='dinner_suggestion_view'),
    path('create_family/', views.create_family, name='create_family'),
    path('show-ip/', views.show_client_ip_view, name='show_client_ip_view'),
    path('dinner-decision/', views.dinner_decision_view, name='dinner_decision'),
]

