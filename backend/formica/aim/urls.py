from django.urls import path

from .views import *

urlpatterns = [
    path('get_all_aims', GetUserAimsView.as_view()),
]
