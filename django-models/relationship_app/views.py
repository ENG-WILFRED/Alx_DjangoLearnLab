from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from .models import UserProfile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book, Author
from django import forms


# Form to use in add/edit views
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]


# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'books': books}  # Use 'books' as the key, matching your template
    return render(request, "relationship_app/list_books.html", context)


@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Book added successfully!")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})


@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse("Book updated successfully!")
    else:
        form = BookForm(instance=book)
    return render(
        request, "relationship_app/edit_book.html", {"form": form, "book": book}
    )


@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return HttpResponse("Book deleted successfully!")
    return render(request, "relationship_app/delete_book.html", {"book": book})


@user_passes_test(
    lambda u: u.is_authenticated
    and hasattr(u, "userprofile")
    and u.userprofile.role == "Admin"
)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(
    lambda u: u.is_authenticated
    and hasattr(u, "userprofile")
    and u.userprofile.role == "Librarian"
)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(
    lambda u: u.is_authenticated
    and hasattr(u, "userprofile")
    and u.userprofile.role == "Member"
)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# Registration view (Class-Based)
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "relationship_app/register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect("list_books")
        return render(request, "relationship_app/register.html", {"form": form})


# Class-based view: Show a specific library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
