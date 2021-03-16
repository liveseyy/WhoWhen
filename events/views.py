from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Event


class EventCreate(CreateView):
    model = Event
    fields = ['title', 'description', 'date_start', 'date_end']


class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'
