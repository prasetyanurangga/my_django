from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:category_id>', views.detail, name='detail'),
	path('all/', views.all, name='all'),
	path('add_category/', views.add_category, name='add_category'),
	path('set_cookies/', views.setCookies, name='set_cookies'),
	path('get_cookies/', views.getCookies, name='get_cookies'),
]
