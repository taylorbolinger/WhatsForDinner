from django.urls import path
from . import views
from .views import signup, logout_view, user_login, dinner_options_view, dinner_suggestion_view, show_client_ip_view

urlpatterns = [
    path('', views.index, name='index'),  
    path('index/', views.index, name='index'),  
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('login/', user_login, name='login'),
    path('dinner-options/', dinner_options_view, name='dinner_options_view'),
    path('dinner-suggestions/', dinner_suggestion_view, name='dinner_suggestion_view'),
    path('show-ip/', show_client_ip_view, name='show_client_ip_view'),
]