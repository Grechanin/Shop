from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import *
app_name="landing"

urlpatterns = [
    url(r'^landing/$', LandingCreateView.as_view(), name='landing'),
    url(r'^$', home, name='home'),
]
