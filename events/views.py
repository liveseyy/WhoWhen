from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Event
from .forms import EventForm


class EventCreate(CreateView):
    model = Event
    form_class = EventForm


class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'
