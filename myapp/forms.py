from django import forms

class CategoryForm(forms.Form):
	"""docstring for CategoryForm"""
	title = forms.CharField(max_length = 100)
	image = forms.FileField(label = 'select a file')