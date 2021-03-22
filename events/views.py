import datetime
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from .models import Event, MemberDates
from .forms import EventForm, MemberForm
from .services.event_dates import get_days_between_dates_json, get_days_between_dates_datetime, str_to_int_months
from .services.event_calendar import get_calendar_event


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'

    def post(self, request, slug):
        """Сreates an event member"""
        data = request.POST
        form = MemberForm(data=data)
        event = self.get_object()
        if form.is_valid():
            member = form.save(commit=False)
            member.event = event
            member.save()
            if data['dates']:
                for date_raw in data.getlist('dates'):
                    date_raw = date_raw.split('.')
                    date = datetime.date(year=int(date_raw[0]), month=str_to_int_months[date_raw[1]], day=int(date_raw[2]))
                    MemberDates.objects.create(member=member, date=date)
        return redirect(event.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_form'] = MemberForm()

        event = context['event']

        dates_between_event_json = get_days_between_dates_json(event)
        context['dates_between'] = dates_between_event_json

        event_members = event.members.all()
        dates_between_event = get_days_between_dates_datetime(event)
        context['graphic'] = get_calendar_event(event_members, dates_between_event)
        # context['days_when_lot_ready'] = get_days_when_lot_ready(event_members, dates_between_event)
        return context
