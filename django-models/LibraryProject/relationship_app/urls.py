from django.urls import path
from .views import list_books, LibraryDetailView, RegisterView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

from .views import (
    list_books, LibraryDetailView,
    RegisterView, admin_view, librarian_view, member_view
)

urlpatterns = [
    path('admin-only/', admin_view, name='admin_view'),
    path('librarian-only/', librarian_view, name='librarian_view'),
    path('member-only/', member_view, name='member_view'),

    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),

    # Auth routes
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
