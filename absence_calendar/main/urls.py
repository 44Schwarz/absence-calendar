from django.conf.urls import url
from . import views

urlpatterns = [
    url('calendar', views.calendar_view),
]
