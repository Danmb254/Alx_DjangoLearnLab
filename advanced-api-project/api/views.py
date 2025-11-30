from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ✔ Retrieve all books (Read-Only)
class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Accessible to both authenticated and non-authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ✔ Retrieve one book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns details of a single book using its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ✔ Create a new book (Authenticated only)
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.
    Custom validation of publication_year happens in serializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # OPTIONAL: Auto-set author if desired
    def perform_create(self, serializer):
        serializer.save()


# ✔ Update an existing book (Authenticated only)
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update book information.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ✔ Delete a book (Authenticated only)
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]