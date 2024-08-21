from django.urls import path
from . import views

urlpatterns = [
    path('new_user/', views.new_user, name='new_user'),
    path('get_users/', views.get_users, name='get_users'),

]