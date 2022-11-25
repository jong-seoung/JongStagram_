from django.urls import path
from .views import Join, login

urlpatterns = [
    path('join',Join.as_view()),
    path('login',login.as_view())
]
