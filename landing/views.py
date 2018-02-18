from django.views.generic import  CreateView, ListView
from django.shortcuts import render
from .forms import *
from products.models import *

class LandingCreateView(CreateView):
	form_class = SubscriberForm
	template_name = 'landing/form.html'
	success_url = '/landing/'
	def get_context_data(self, *args, **kwargs):
		context = super(LandingCreateView, self).get_context_data(*args, **kwargs)
		context['title']='Реєстрація'
		return context

# class HomeView(ListView):
# 	def get_queryset(self):
# 		return Product.objects.all()#[:4]

def home(request):
	product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)[:4]
	product_images_phones = ProductImage.objects.filter(product__category__name='phones', is_active=True, is_main=True, product__is_active=True)[:4]
	product_images_laptops = ProductImage.objects.filter(product__category__name='laptops', is_active=True, is_main=True, product__is_active=True)[:4]
	return render(request, 'home.html', locals())

