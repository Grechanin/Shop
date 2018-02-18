from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import *
app_name="products"

urlpatterns = [
    # url(r'^landing/', LandingCreateView.as_view(), name='home'),
    url(r'^product/(?P<product_id>\w+)/$', product, name='product'),
]
