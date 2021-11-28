# api_final
Данный проект является реализацией API для сервиса yatube

### Как запустить проект:
Клонировать и перейти в другую репозиторий:
```
git clone https://github.com/yandex-praktikum/kittygram.git
```
```
cd kittygram
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Установить зависимость из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
### Примеры:
Получить все посты:

URL: http://127.0.0.1:8000/api/v1/posts/

Method: GET

Response (JSON):
```
[
    {
        "id": 1,
        "author": "user",
        "text": "some text",
        "pub_date": "2021-11-28T08:14:49.135745Z",
        "image": null,
        "group": 1
    }
]
```
Создать комментарий к посту:

URL: http://127.0.0.1:8000/api/v1/posts/1/comments/

Method: POST

Request (JSON):
```
{
    "text": "comment"
}
```

Response (JSON):
```
{
    "id": 1,
    "author": "user",
    "post": 1,
    "text": "comment",
    "created": "2021-11-28T12:33:52.326816Z"
}
```
Обновить пост:

URL: http://127.0.0.1:8000/api/v1/posts/1/

Method: PATCH

Request (JSON):
```
{
    "text": "updating"
}
```

Response (JSON):
```
{
    "id": 1,
    "author": "user",
    "text": "updating",
    "pub_date": "2021-11-28T08:14:49.135745Z",
    "image": null,
    "group": null
}
```
-----
##### Более подробную инструкцию можно найти в самом проекте по адресу ```http://127.0.0.1:8000/redoc/```
