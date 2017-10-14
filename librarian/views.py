from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Book


# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'librarian/book_list.html', {'books': books})
