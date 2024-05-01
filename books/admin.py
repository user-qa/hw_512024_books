from django.contrib import admin
from books.models import BookModel

@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'page']
    list_filter = ['title']