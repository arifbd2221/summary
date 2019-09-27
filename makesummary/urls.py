from django.urls import path
from .views import generatesummary

urlpatterns = [
    path('summary/', generatesummary, name='summary'),
]