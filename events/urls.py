from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventCreateView.as_view(), name='event_create'),
    path('<slug:slug>/', views.EventDetailView.as_view(), name='event_detail'),
]
