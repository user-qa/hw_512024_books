from django.shortcuts import render

from books.models import BookModel


def BookView(request):
    books = BookModel.objects.all()
    context = {
        'books_list': books
    }
    return render(request, 'index.html', context= context)