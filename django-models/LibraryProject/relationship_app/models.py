from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# -----------------------------
# Author model
# -----------------------------
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# -----------------------------
# Book model
# -----------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

# -----------------------------
# Intermediate model for M2M
# -----------------------------
class LibraryBooks(models.Model):  # must match 'through="LibraryBooks"' in Library
    library = models.ForeignKey('Library', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.library.name} - {self.book.title}"

# -----------------------------
# Library model
# -----------------------------
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, through='LibraryBooks', related_name='libraries')

    def __str__(self):
        return self.name

# -----------------------------
# Librarian model
# -----------------------------
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name

# -----------------------------
# UserProfile model
# -----------------------------
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Automatically create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
