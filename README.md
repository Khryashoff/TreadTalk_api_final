# Api_final
## Description
An innovative social network for micro-blogs, and maybe not so micro. 
In this iteration of the project, interaction with the API functionality has become available. Using the API, users, as well as third-party services and applications can interact with the project database, including viewing, editing, deleting posts and commentaries, etc. Some of the functionality is available only to authorized users, please register.

## Technologies
- Python 3.9.10
- Django 3.2.16
- Django REST framework 3.12.4
- JWT + Djoser

## Launching a project in dev mode
1. Clone the repository and go to it on the command line:
```bash
git clone https://github.com/Khryashoff/api_final_yatube.git
```
```bash
cd api_final_yatube/
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
```
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
```
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
```
GET /api/v1/posts/?limit=10&offset=5
```

- In order to create a publication:
```
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
```
PUT /api/v1/posts/{id}/
PATCH /api/v1/posts/{id}/
DEL /api/v1/posts/{id}/
```

- To create a comment:
```
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
```
# Project documentation
http://127.0.0.1:8000/redoc/
```

## Authors
Sergey Khryashchev [(Khryashoff)](https://github.com/Khryashoff)