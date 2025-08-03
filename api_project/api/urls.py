from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns += [
    path('auth-token/', obtain_auth_token),
]
