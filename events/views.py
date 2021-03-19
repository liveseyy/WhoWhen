from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, DetailView
from .models import Event, Member
from .forms import EventForm, MemberForm
from .services import get_days_between_dates


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'

    def post(self, request, slug):
        data = request.POST
        form = MemberForm(data=data)
        event = self.get_object()
        if form.is_valid():
            member = form.save(commit=False)
            member.event = event
            member.date_when_can = data.getlist('dates')
            member.save()
        return redirect(event.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_form'] = MemberForm()

        event = context['event']
        dates_between = get_days_between_dates(event)
        context['dates_between'] = dates_between
        return context
