from django import forms

from .models import Subscriber
from .models import *

class SubscriberForm(forms.ModelForm):
	class Meta:
		model = Subscriber
		#fields = [""]
		exclude = [""]