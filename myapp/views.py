from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader, RequestContext
from .models import Category
from .forms import CategoryForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
	return HttpResponse("hello Angga")

def all(request):
	list_category = Category.objects.all()
	return render(request, 'list_category.html',{
		'list_category': list_category,
	})

def detail(request, category_id):
	category =  get_object_or_404(Category, pk=category_id)
	return render(request, 'detail_category.html',{
		'category' : category,
	})

def add_category(request):
	try:
		if request.method == "POST":
			categoryForm = CategoryForm(request.POST, request.FILES)
			if categoryForm.is_valid():
				imageFile = categoryForm.cleaned_data['image']
				fs = FileSystemStorage()
				filename = fs.save(imageFile.name, imageFile)
				uploaded_file_url = fs.url(filename)
				print(uploaded_file_url)
				category = Category()
				category.title = categoryForm.cleaned_data['title']
				category.image = categoryForm.cleaned_data['image']
				category.save()
				return redirect('myapp:all')
			else:
				form = CategoryForm()
				return render(request, 'add_category.html',{
					'error_message' : 'Erorr',
					'form' : form,
				})	
		else:
			form = CategoryForm()
			return render(request, 'add_category.html',{
				'error_message' : '',
				'form' : form,
			})
	except Exception as e:
		form = CategoryForm()
		return render(request, 'add_category.html',{
			'error_message' : 'Erorr',
			'form' : form,
		})

def setCookies(request):
	username = "angga"
	response = render(request, 'test_view.html', { 'username' : username })
	response.set_cookie('username', username, max_age=300)
	return response

def getCookies(request):
	username = request.COOKIES['username']
	return 	render(request, 'test_view.html', { 'username' : username })