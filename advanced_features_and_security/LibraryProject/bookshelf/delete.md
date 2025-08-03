```python
from bookshelf.models import Book

# Delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify it's deleted
Book.objects.all()
