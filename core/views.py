from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Book
from .permissions import IsSuperUserOrReadOnly
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """Viewset Для работы с книгами."""

    # Используем select_related.
    # Это позволит одним JOIN запросом из БД получить все книги и их авторов.
    # А также поможет избежать проблемы N+1 при  большом количестве записей.
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer

    # Используем кастомный пермишен.
    # Это упростит логику выдачи разрешений пользователям.
    # Безопасные запросы для всех, небезопасные только для superusers.
    permission_classes = [IsSuperUserOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["author", "publication_year"]
    ordering_fields = ["title"]  # Сортировка по названию (A-Z и Z-A)
