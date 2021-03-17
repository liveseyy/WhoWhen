from django import forms
from django.forms import ValidationError
from .models import Event, Member


class EventForm(forms.ModelForm):
    title = forms.CharField(label='Название')
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 35, 'rows': 5}), required=False)
    date_start = forms.DateField(label='Дата начала', input_formats=['%d.%m.%Y'])
    date_end = forms.DateField(label='Дата окончания', input_formats=['%d.%m.%Y'])

    def clean_date_end(self):
        date_end = self.cleaned_data.get('date_end')
        date_start = self.cleaned_data.get('date_start')
        try:
            if date_end < date_start:
                raise ValidationError("Дата окончания должна быть после даты начала!")
        except TypeError:
            pass
        return date_end
    
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_start', 'date_end']


class MemberForm(forms.ModelForm):
    name = forms.CharField(label='Имя')

    class Meta:
        model = Member
        fields = ['name']
