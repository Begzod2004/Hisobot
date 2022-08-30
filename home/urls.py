from django.urls import *
from .views import *
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', HisobotListView.as_view(), name='Hisobot-main'),
    path('Hisobot', HisobotListView.as_view(), name='Hisobot-main1'),
    path('Hisobot/add', HisobotCreateView.as_view(), name='Hisobot'),
    path('Hisobot/<int:pk>', HisobotDetailView.as_view(), name='hisobot-detail'),
    path('Daromad/add', DarmadCreateView.as_view(), name='Daromad-add'),
    path('Harajatlar/add', XarajatlarCreateView.as_view(), name='harajat-add'),
    path('Drektor/add', DrektorCreateView.as_view(), name='drektor-add'),
    path('Drektor/', DrektorListView.as_view(), name='drektor-view'),

    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path('profile/', profile, name='profile'),


]
