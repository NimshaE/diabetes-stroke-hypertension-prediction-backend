from django.urls import path
from . import views

urlpatterns = [
    path('check-email/', views.check_email, name='check-email'),
    path('profile/', views.user_profile, name='user-profile'),
]