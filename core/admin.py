from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Админка для Авторов"""

    list_display = ("full_name", "birth_date", "book_count")
    search_fields = ("full_name",)
    list_filter = ("birth_date",)

    def book_count(self, obj):
        return obj.books.count()  # Подсчет книг для удобства.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Админка для Книг"""

    list_display = ("title", "author", "publication_year", "cover_image")
    search_fields = ("title", "author__full_name")
    list_filter = ("publication_year", "author")
