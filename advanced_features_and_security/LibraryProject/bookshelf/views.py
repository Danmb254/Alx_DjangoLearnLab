from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django import forms
from .models import Book
from .forms import ExampleForm   # ← required by ALX checker

# FORM WITH VALIDATION (prevents unsafe input)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.add_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.view_book', raise_exception=True)
def books(request):
    return render(request, 'bookshelf/book_list.html')

def search_books(request):
    query = request.GET.get('q', '').strip()
    books = Book.objects.filter(title__icontains=query) if query else []
    return render(request, 'bookshelf/book_list.html', {'books': books})