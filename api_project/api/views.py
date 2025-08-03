from rest_framework.generics import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
