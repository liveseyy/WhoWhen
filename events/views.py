from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Event
from .forms import EventForm, MemberForm
from .services import get_days_between_dates


class EventCreate(CreateView):
    model = Event
    form_class = EventForm


class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_form'] = MemberForm()

        event = context['event']
        dates_between = get_days_between_dates(event)
        context['dates_between'] = dates_between
        return context
