from ..models import Event
from .event_dates import get_days_between_dates_datetime
import base64
from io import BytesIO
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np


merge_nested_list = lambda s: reduce(lambda d, el: d.extend(el) or d, s, [])


def get_event_calendar(event: Event):
    """
        return colormap-calendar of event with counting the number of people in each day
    """
    event_members = event.members.all()
    member_dates = list(map(lambda member: member.dates.values_list('date', flat=True), event_members))

    member_dates = merge_nested_list(member_dates)

    dates_between_event = get_days_between_dates_datetime(event)

    count_members_on_date = []
    for date in dates_between_event:
        count_members_on_date.append(member_dates.count(date))
    if len(dates_between_event) < 50:
        fig, ax = plt.subplots(figsize=(10, 10))
    else:
        height_graph = 10 + len(dates_between_event)//11
        fig, ax = plt.subplots(figsize=(10, height_graph))
    calendar_heatmap(ax, dates_between_event, count_members_on_date)

    buffer = BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    return graphic


def calendar_array(dates, data):
    i, j = zip(*[d.isocalendar()[1:] for d in dates])
    i = np.array(i) - min(i)
    j = np.array(j) - 1
    ni = max(i) + 1

    calendar = np.nan * np.zeros((ni, 7))
    calendar[i, j] = data
    return i, j, calendar


def calendar_heatmap(ax, dates, data):
    i, j, calendar = calendar_array(dates, data)
    im = ax.imshow(calendar, interpolation='none', cmap=plt.get_cmap('summer', len(set(data))))
    label_days(ax, dates, i, j, calendar)
    label_months(ax, dates, i, j, calendar)
    cbar = ax.figure.colorbar(im)
    cbar.set_ticks([i for i in range(max(data)+1)])

def label_days(ax, dates, i, j, calendar):
    ni, nj = calendar.shape
    day_of_month = np.nan * np.zeros((ni, 7))
    day_of_month[i, j] = [d.day for d in dates]

    for (i, j), day in np.ndenumerate(day_of_month):
        if np.isfinite(day):
            ax.text(j, i, int(day), ha='center', va='center')

    ax.set(xticks=np.arange(7),
           xticklabels=['????', '????', '????', '????', '????', '????', '????'])
    ax.xaxis.tick_top()

def label_months(ax, dates, i, j, calendar):
    month_labels = np.array(['??????', '??????', '??????', '??????', '??????', '????????', '????????',
                             '??????', '??????', '??????', '????????', '??????'])
    months = np.array([d.month for d in dates])
    uniq_months = sorted(set(months))
    yticks = [i[months == m].mean() for m in uniq_months]
    labels = [month_labels[m - 1] for m in uniq_months]
    ax.set(yticks=yticks)
    ax.set_yticklabels(labels, rotation=90)
