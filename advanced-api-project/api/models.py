from django.db import models
from django.utils import timezone

# ---------------------------------------------
# Author Model
# ---------------------------------------------
# Represents a book author.
# One author can have MANY books.
# This model stores basic author information.
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author’s full name

    def __str__(self):
        return self.name


# ---------------------------------------------
# Book Model
# ---------------------------------------------
# Represents a book written by an author.
# The ForeignKey relationship creates:
# Author 1 → Many Books
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"