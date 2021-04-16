import datetime
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from .models import Event, MemberDates
from .forms import EventForm, MemberForm
from .services.event_dates import get_days_between_dates_json, str_to_int_months, get_most_selected_dates
from .services.event_calendar import get_event_calendar


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
            if data.get('dates'):
                for date_raw in data.getlist('dates'):
                    date_raw = date_raw.split('.')
                    date = datetime.date(year=int(date_raw[0]), month=str_to_int_months[date_raw[1]], day=int(date_raw[2]))
                    MemberDates.objects.create(member=member, date=date)
        return redirect(event.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['member_form'] = MemberForm()

        event = context['event']

        context['dates_between'] = get_days_between_dates_json(event)

        context['event_calendar'] = get_event_calendar(event)

        context['days_when_lot_ready'] = get_most_selected_dates(event)
        return context
