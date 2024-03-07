from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name='user-signup'),
    path('login/', views.user_login, name='user-login'),
]