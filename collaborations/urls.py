from django.urls import path
from . import views

app_name = 'collaborations'


urlpatterns = [
    path('signup/', views.user_signup, name='user-signup'),
    path('login/', views.user_login, name='user-login'),
    path('profile/', views.profile_view, name='user-profile_view'),
]