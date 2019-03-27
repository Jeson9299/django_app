from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib import messages
from .forms import ModelForm


# Create your views here.
def home(request):
	if request.method == 'POST':
		form=ModelForm(request.POST, request.FILES)
		if form.is_valid():
#			img = Post(handle_uploaded_file(request.FILES['image']))
#			img.save()
			form.save()
			messages.success(request, f'Thank You!!')
			return redirect('main_page-lost')
	else:
		form=ModelForm()
	return render(request, 'main_page/home.html', {'form' : form})

def lost(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'main_page/lost.html', context)

