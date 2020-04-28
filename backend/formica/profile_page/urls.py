from django.urls import path

from .views import *

urlpatterns = [
    path('', ProfilePageInfoView.as_view()),
]