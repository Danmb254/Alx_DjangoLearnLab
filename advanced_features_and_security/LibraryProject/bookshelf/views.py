from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book  # make sure Book exists in bookshelf/models.py

# ---------------------------
# Book List View
# ---------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # variable 'books' is required
    return render(request, 'bookshelf/book_list.html', {'books': books})
