from django.test import SimpleTestCase
from django.urls import reverse, resolve
from events.views import EventCreateView, EventDetailView


class TestUrls(SimpleTestCase):

    def test_event_create_url_is_resolved(self):
        url = reverse('event_create')
        self.assertEqual(resolve(url).func.view_class, EventCreateView)

    def test_event_detail_url_is_resolved(self):
        url = reverse('event_detail', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, EventDetailView)
