from django.urls import path
from . import views

app_name = 'projects'


urlpatterns = [
    path('add/', views.create_project, name='add_project'),
]