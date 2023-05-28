from django.contrib import admin

from api.tracker.models import Protocol, Exercise, Entries

admin.site.register(Protocol)
admin.site.register(Exercise)
admin.site.register(Entries)

