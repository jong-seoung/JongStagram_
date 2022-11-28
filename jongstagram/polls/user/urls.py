from django.urls import path
from .views import Join, login, logout, Uploadprofile

urlpatterns = [
    path('join',Join.as_view()),
    path('login',login.as_view()),
    path('logout',logout.as_view()),
    path('profile/upload',Uploadprofile.as_view())
]

