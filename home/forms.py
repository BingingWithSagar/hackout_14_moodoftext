from django import forms
from .models import post
from django.forms import ModelForm

class postform(ModelForm):
	class Meta:
		model = post
		fields=['title','entry']

