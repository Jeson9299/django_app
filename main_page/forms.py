from django import forms
from .models import Post

class ModelForm(forms.ModelForm):
	#field_order = ['image', 'breed', 'name', 'contact', 'address', 'additional_info', ]
#	image = forms.ImageField()
#	breed = forms.CharField(max_length=100)
#	name = forms.CharField(max_length=100)
#	contact = forms.IntegerField()
#	address = forms.CharField()
#	additional_info = forms.CharField()
	#date_posted = forms.DateTimeField(default=timezone.now())

	class Meta:
		model = Post
		fields = ('image', 'breed', 'name', 'contact', 'address', 'additional_info',)