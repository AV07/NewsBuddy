from django.urls import path
from accounts.views import *

app_name = 'account'

urlpatterns = [
    path('register/',UserRegistrationView,name="register"),
    path('login/',UserLoginView,name="login"),
]