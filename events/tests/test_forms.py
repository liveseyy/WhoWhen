from django.test import SimpleTestCase
from events.forms import EventForm, ValidationError


class TestForms(SimpleTestCase):

    def test_event_form_valid_data(self):
        form = EventForm(data={
            'title': 'Birthday',
            'date_start': '16.04.2020',
            'date_end': '17.04.2020'
        })

        self.assertTrue(form.is_valid())

    def test_event_form_invalid_date_data(self):
        form1 = EventForm(data={
            'title': 'Birthday',
            'date_start': '17.04.2020',
            'date_end': '16.04.2020'
        })
        form2 = EventForm(data={
            'title': '',
            'date_start': '',
            'date_end': ''
        })

        self.assertFalse(form1.is_valid())
        self.assertFalse(form2.is_valid())
        self.assertEqual(len(form1.errors), 1)
        self.assertEqual(len(form2.errors), 3)



