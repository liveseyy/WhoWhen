from django.contrib import admin
from .models import Event, Member


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass
