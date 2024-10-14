# TreadTalk_api_final

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)
![Django REST framework](https://img.shields.io/badge/-Django%20REST%20framework-ff9900?style=flat&logo=django&logoColor=white)

# Russian version
*Note: The English version of this document is also available [here](https://github.com/Khryashoff/TreadTalk_api_final#english-version).*

## Финальная версия API для приложения TreadTalk.

Доступные функции для взаимодействия с API проекта:  
- Получать токен аутентификации, передав логин и пароль
- Получать список всех постов или создавать новый
- Получать конкретный пост, редактировать или удалять его по id
- Получать список всех групп
- Получить информацию о группе по id
- Получать список всех комментариев поста с id=post_id или создавать новый
- Получать, редактировать или удалять комментарий по id y поста с id=post_id
- Оформлять подписку на автора публикации
- Оформлять подписку на группу 
- Получать список всех подписчиков текущего пользователя

## Технологии 
- Python 3.9.10 
- Django 3.2.16 обновлено до Django 4.2.16
- Django REST framework 3.12.4 обновлено до DRF 3.15.2
- JWT 2.9.0
- Djoser 2.2.3

## Запуск проекта в режиме разработки
1. Клонируем репозиторий и переходим к нему из командной строки:
```bash
git clone https://github.com/Khryashoff/TreadTalk_api_final
```
2. Установите и активируйте виртуальную среду для проекта:
```bash
python -m venv venv
```
```bash
# for OS Windows
. venv/Scripts/activate
```
3. Обновите pip и установите зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
4. Выполните миграцию на уровне проекта:
```bash
python manage.py migrate
```
5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
6. Запустите проект:
```bash
python manage.py runserver
```

## Примеры запросов
### Работа с API проекта для неавторизованных пользователей
Для неавторизованных пользователей работа с API доступна только в режиме чтения, редактирование и удаление записей недоступно.
```http
GET api/v1/posts/ - get a list of all publications.
If you specify the parameters limit (number of objects) and offset (from which object to start counting), data output will be performed with pagination
GET api/v1/posts/{id}/ - getting a publication by id
GET api/v1/{post_id}/comments/ - getting all comments for publication
GET api/v1/{post_id}/comments/{id}/ - Getting a comment on a publication by id
GET api/v1/groups/ - getting a list of available communities
GET api/v1/groups/{id}/ - getting information about the community by id
```

### Работа с API проекта для авторизованных пользователей

- Получение токена для авторизованного пользователя.
```http
POST /api/v1/jwt/create/
```

Pass user data to body:
```json
{
"username": "string",
"password": "string"
}
```

Укажите полученный токен в поле авторизации, чтобы получить доступ ко всему функционалу проекта:
```
Authorization: Bearer {your_token}
```

- Для того, чтобы активировать разбивку на страницы:
```http
GET /api/v1/posts/?limit=10&offset=5
```

- Для того, чтобы создать публикацию:
```http
POST /api/v1/posts/
```

Пример тела ответа:
```json
{
  "id": 1,
  "author": "UserName",
  "text": "Publication",
  "pub_date": "2023-04-16T18:00:00.021094Z",
  "image": null,
  "group": null
}
```

- Для того, чтобы полностью (PUT) или частично (PACTH) обновить или удалить (DEL) публикацию:
```http
PUT /api/v1/posts/{id}/
PATCH /api/v1/posts/{id}/
DEL /api/v1/posts/{id}/
```

- Чтобы создать комментарий:
```http
POST /api/v1/posts/{post_id}/comments/
```

Пример тела ответа:
```json
{
  "id": 1,
  "author": "UserName",
  "text": "Comment",
  "created": "2023-04-16T18:00:00.021094Z",
  "post": 1
}
```

## Ресурсы
```bash
# Project documentation
http://127.0.0.1:8000/redoc/
```

## Authors
Сергей Хрящев [(Khryashoff)](https://github.com/Khryashoff)

---

# English version

## Technologies
- Python 3.9.10 
- Django 3.2.16 update to Django 4.2.16
- Django REST framework 3.12.4 update to DRF 3.15.2
- JWT 2.9.0
- Djoser 2.2.3

## Launching a project in dev mode
1. Clone the repository and go to it on the command line:
```bash
git clone https://github.com/Khryashoff/TreadTalk_api_final
```
2. Install and activate the virtual environment for the project:
```bash
python -m venv venv
```
```bash
# for OS Windows
. venv/Scripts/activate
```
3. Update pip and install dependencies from the file requirements.txt:
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
4. Perform migrations at the project level:
```bash
python manage.py migrate
```
5. Create a superuser:
```bash
python manage.py createsuperuser
```
6. Start the project:
```bash
python manage.py runserver
```

## Request examples
### Working with the project API for unauthorized users
For unauthorized users, working with the API is only available in read mode, editing and deleting records is not available.
```http
GET api/v1/posts/ - get a list of all publications.
If you specify the parameters limit (number of objects) and offset (from which object to start counting), data output will be performed with pagination
GET api/v1/posts/{id}/ - getting a publication by id
GET api/v1/{post_id}/comments/ - getting all comments for publication
GET api/v1/{post_id}/comments/{id}/ - Getting a comment on a publication by id
GET api/v1/groups/ - getting a list of available communities
GET api/v1/groups/{id}/ - getting information about the community by id
```

### Working with the project API for authorized users

- Getting a token for an authorized user.
```http
POST /api/v1/jwt/create/
```

Pass user data to body:
```json
{
"username": "string",
"password": "string"
}
```

Specify the received token in the Authorization field to access the full functionality of the project:
```
Authorization: Bearer {your_token}
```

- In order to activate pagination:
```http
GET /api/v1/posts/?limit=10&offset=5
```

- In order to create a publication:
```http
POST /api/v1/posts/
```

Example of a response in body:
```json
{
  "id": 1,
  "author": "UserName",
  "text": "Publication",
  "pub_date": "2023-04-16T18:00:00.021094Z",
  "image": null,
  "group": null
}
```

- In order to completely (PUT) or partially (PATCH) update or delete (DEL) a publication:
```http
PUT /api/v1/posts/{id}/
PATCH /api/v1/posts/{id}/
DEL /api/v1/posts/{id}/
```

- To create a comment:
```http
POST /api/v1/posts/{post_id}/comments/
```

Example of a response in body:
```json
{
  "id": 1,
  "author": "UserName",
  "text": "Comment",
  "created": "2023-04-16T18:00:00.021094Z",
  "post": 1
}
```

## Resources
```bash
# Project documentation
http://127.0.0.1:8000/redoc/
```

## Authors
Sergey Khryashchev [(Khryashoff)](https://github.com/Khryashoff)
