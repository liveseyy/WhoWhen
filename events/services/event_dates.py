from datetime import timedelta
from ..models import Event

en_to_ru_months = {
    'January': 'Январь', 'February': 'Февраль', 'March': 'Март', 'April': 'Апрель',
    'May': 'Май', 'June': 'Июнь', 'July': 'Июль', 'August': 'Август',
    'September': 'Сентябрь', 'October': 'Октябрь', 'November': 'Ноябрь', 'December': 'Декабрь'
}

str_to_int_months = {
    'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4,
    'Май': 5, 'Июнь': 6, 'Июль': 7, 'Август': 8,
    'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12
}


def get_days_between_dates_json(event: Event):
    """return dictionary of event dates like
                            {'year': {
                                'month1': [days],
                                'month2': [days],
                                ...
                                }
                            }
    """
    date_delta = event.date_end - event.date_start
    dates_between = dict()
    date_start = event.date_start
    for i in range(date_delta.days + 1):
        year = date_start.year
        month = en_to_ru_months[date_start.strftime("%B")]
        day = date_start.day
        if dates_between.get(year, None):
            if dates_between[year].get(month, None):
                dates_between[year][month].append(day)
            else:
                dates_between[year][month] = [day]
        else:
            dates_between[year] = {month: [day]}
        date_start = date_start + timedelta(days=1)
    return dates_between


def get_days_between_dates_datetime(event: Event):
    """
        return a list with objects datetime.date of event
    """

    date_delta = event.date_end - event.date_start
    dates_between = []
    date_start = event.date_start
    for i in range(date_delta.days + 1):
        dates_between.append(date_start)
        date_start = date_start + timedelta(days=1)
    return dates_between
