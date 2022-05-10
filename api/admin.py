from dataclasses import fields
from django.contrib import admin

from api.models import Contact, Event


# # Register your models here.
class ContactAdmin(admin.StackedInline):
    model = Contact
    fields = ('name', 'phone')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    inlines = (ContactAdmin, )

    class Meta:
        model = Event