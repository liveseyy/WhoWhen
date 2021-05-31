from django import forms
from django.forms import ValidationError
from django.utils import timezone, dateformat
from .models import Event, Member
from datetime import timedelta


class EventForm(forms.ModelForm):
    title = forms.CharField(label='Название', label_suffix='', widget=forms.TextInput(attrs={'autocomplete': "off"}),
                            max_length=200)
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 35, 'rows': 3, 'autocomplete': "off"},),
                                  required=False, label_suffix='', max_length=255)
    date_start = forms.DateField(label='Дата начала',
                                 widget=forms.TextInput(
                                     attrs={'placeholder': dateformat.format(timezone.now(), 'd.m.Y'),
                                            'autocomplete': "off"}),
                                 input_formats=['%d.%m.%Y'], label_suffix='')
    date_end = forms.DateField(label='Дата окончания',
                               widget=forms.TextInput(
                                   attrs={'placeholder': dateformat.format(timezone.now() + timedelta(days=31), 'd.m.Y'),
                                          'autocomplete': "off"}),
                               input_formats=['%d.%m.%Y'], label_suffix='')

    def clean(self):
        data = super(EventForm, self).clean()
        date_end = data.get('date_end')
        date_start = data.get('date_start')
        if date_end and date_start:
            if date_end < date_start:
                raise ValidationError("Дата окончания должна быть после даты начала.")
        return self.cleaned_data

    class Meta:
        model = Event
        fields = ['title', 'description', 'date_start', 'date_end']


class MemberForm(forms.ModelForm):
    name = forms.CharField(label='Имя', max_length=100)

    class Meta:
        model = Member
        fields = ['name']
