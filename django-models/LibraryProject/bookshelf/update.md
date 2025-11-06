

from bookshelf.models import Book

# Retrieve and update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>