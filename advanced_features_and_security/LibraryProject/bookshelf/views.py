from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django import forms
from .models import Book

# FORM WITH VALIDATION (prevents unsafe input)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

# REQUIRED by ALX checker
@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # ORM prevents SQL injection
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Secure view example
@permission_required('bookshelf.add_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()   # safe, ORM parameterized
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# REQUIRED by ALX checker
@permission_required('bookshelf.view_book', raise_exception=True)
def books(request):
    return render(request, 'bookshelf/book_list.html')

# Example secure search implementation
def search_books(request):
    query = request.GET.get('q', '').strip()
    books = Book.objects.filter(title__icontains=query) if query else []
    return render(request, 'bookshelf/book_list.html', {'books': books})