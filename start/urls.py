from django.urls import path

from start.views.UsersView import API as uss

urlpatterns = [
    path('uss', uss.user)
]