from django.contrib import admin
from .models import Event, Member, MemberDates


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(MemberDates)
class MemberDatesAdmin(admin.ModelAdmin):
    pass
