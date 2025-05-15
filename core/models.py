from django.db import models

from library.constants import TEXT_LENGTH


class Author(models.Model):
    """Модель автора произведения."""
    full_name = models.CharField(
        max_length=TEXT_LENGTH,
        verbose_name="ФИО",
        db_index=True
    )
    birth_date = models.DateField(verbose_name="Дата рождения")
    biography = models.TextField(verbose_name="Биография", blank=True)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    """Модель произведения."""
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name="Автор"
    )
    title = models.CharField(
        max_length=TEXT_LENGTH,
        verbose_name="Название",
        db_index=True)  # Индексация для ускорения сортировки/поиска
    publication_year = models.PositiveIntegerField(
        verbose_name="Год издания",
        db_index=True
    )
    preface = models.TextField(verbose_name="Предисловие", blank=True)
    cover_image = models.ImageField(
        upload_to="book_covers/",
        verbose_name="Обложка",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
