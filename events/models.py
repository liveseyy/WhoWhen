from django.db import models
from django.shortcuts import reverse
from django.utils.crypto import get_random_string


class Event(models.Model):
    """The event that people are going to"""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    date_start = models.DateField()
    date_end = models.DateField()
    date_create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.title}({self.date_start} до {self.date_end})'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_random_string(length=15)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('event_detail', args=[self.slug])


class Member(models.Model):
    """Member of event"""
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, related_name="members", on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.name}" go on {self.event.title}'


class MemberDates(models.Model):
    """Dates when member can go"""
    member = models.ForeignKey(Member, related_name='dates', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.member.name} - {self.date}'
