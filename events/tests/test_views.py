from django.test import TestCase, Client
from django.urls import reverse
from events.models import Event
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.event_create_url = reverse('event_create')
        self.event_detail_url = reverse('event_detail', args=['slug'])
        self.event = Event.objects.create(
            title='test_event1',
            date_start='2020-01-01',
            date_end='2020-01-02',
            slug='slug'
        )

    def test_event_create_GET(self):
        response = self.client.get(self.event_create_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_form.html')

    def test_event_create_POST(self):
        response = self.client.post(self.event_create_url, {
            'title': 'test_event2',
            'date_start': '14.04.2021',
            'date_end': '15.04.2021'
        })
        # Объект не создается, fix

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Event.objects.count(), 2)

    def test_event_create_POST_no_data(self):
        response = self.client.post(self.event_create_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Event.objects.all().count(), 1)

    def test_event_detail_GET(self):
        response = self.client.get(self.event_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_detail.html')

    def test_event_detail_POST_add_member(self):
        response = self.client.post(self.event_detail_url, {
            'name': 'Dima'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.event.members.first().name, 'Dima')
