from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventCreate.as_view(), name='event_create'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
]
