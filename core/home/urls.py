

from django.urls import path
from .views import home, usapage, userList




urlpatterns = [
    path('home/',home, name="home"),
    path('usa/',usapage, name="usapage"),
    path('userlist/',userList, name="userList"),
]