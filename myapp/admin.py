from django.contrib import admin
from .models import Category, Note

class NoteAdmin(admin.ModelAdmin):
	"""docstring for NoteAdmin"""
	fieldsets = [
		(None, {'fields': ['category']}),
		('Detail', {'fields' : ['title','body']}),
	]
	list_display = ('category', 'title', 'body')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id','title','image')
	list_editable = ('title','image')		
	list_filter = ['title']	

admin.site.register(Category, CategoryAdmin)
admin.site.register(Note, NoteAdmin)