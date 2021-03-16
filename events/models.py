from django.db import models


class Event(models.Model):
    """The nearest event that people are going to"""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.date_create.day}.{self.date_create.month}.{self.date_create.year}'


class Member(models.Model):
    """Member of event"""
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, related_name="members", on_delete=models.CASCADE)
    date_when_can = models.JSONField()

    def __str__(self):
        return f'{self.name} go on {self.event.title}'
