from django.urls import path

from . import views

app_name = "tracker"

urlpatterns = [
    path("test/", views.test, name="test"),
    path("protocol/entries/", views.get_protocol_entries_by_user, name="protocol_entries"),
]