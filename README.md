# Library  

**Library** — это REST API-сервис для управления базой книг и авторов.

### Функциональность
- Модели: Автор (ФИО, дата рождения, автобиография), Книга (автор, год издания, название, предисловие, обложка).
- Получение списка книг с фильтрацией по автору и году издания.
- Сортировка книг по названию (A-Z и Z-A).
- Получение книги по ID.
- Добавление и удаление книг — только для суперпользователей.


## Стек технологий
- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite
- Django Filter

## Документация
**Полное описание API доступно после выполнения следующих шагов** :

1. Клонируйте репозиторий:

    git clone https://github.com/your_username/your_project.git
    cd your_project

2. Создайте виртуальное окружение и активируйте его:

    python -m venv venv
    source venv/Scripts/activate

3. Установите зависимости:

    pip install -r requirements.txt

4. Выполните миграции и создайте суперпользователя (в новом терминале):

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

5. Загрузите фикстуры:

    python manage.py loaddata fixtures/initial_data.json

6. Запустите сервер:

    python manage.py runserver


## Сервис будет доступен по следующему адресу 

    http://localhost:8000/api/


### Автор
 Севастиан Долбилин
 Python backend developer