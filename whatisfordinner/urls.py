from django.urls import path
from . import views
from .views import signup, logout_view, user_login

urlpatterns = [
    #path('', views.hello_world, name='hello_world'),
    path('', views.index, name='index'),  
    path('index/', views.index, name='index'),  
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('login/', user_login, name='login'),
]