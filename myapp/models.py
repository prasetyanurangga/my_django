from django.db import models
import uuid
# Create your models here.

class Category(models.Model):
	"""docstring for Category"""
	def __str__(self):
		return self.title
	id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
	title = models.CharField(max_length=100)
	image = models.FileField(upload_to='image/%Y/%m/%d')

class Note(models.Model):
	"""docstring for Note"""
	def __str__(self):
		return self.title
	id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	body = models.TextField()
	title = models.CharField(max_length=100)
