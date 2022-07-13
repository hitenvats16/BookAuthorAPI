
# BookAuthorAPI

A REST API developed in python and Django


## Installation

### Clone Repository into a folder
```bash
  git clone https://github.com/hitenvats16/BookAuthorAPI.git
```

### Install dependencies with pip3

```bash
  pip3 install -r requirements.txt
```

### Change directory to BookAuthorAPI

```bash
  cd BookAuthorAPI/
```

### Creating .env file and adding content to it

```bash
  touch .env
```

After that, you'll need to add `DJANGO_SECRET_KEY` variable with a key to `.env` file

For example: (can be temporarily used in project)
`DJANGO_SECRET_KEY = 'django-insecure-b260ofpg5o(!vkbgu%df30!rf80r$^k71-!qqjqcld&@d4aak!'`

### Migrating Database

```bash
  python manage.py makemigrations
  python manage.py makemigrations author
  python manage.py makemigrations books
  python manage.py migrate
```

### Generating Random Data in Database (Optional)

```bash
  python manage.py createdata
```

### Starting the project

```bash
  python manage.py runserver
```


## API Reference

#### Get Authentication Token

```http
  POST /author/token/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Username for Account |
| `password` | `string` | **Required**. Password for Account |

#### Get List of Authors

```http
  GET /author/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Auth Token for authenticating the user (Passed in header) |

#### Get Current Author Info

```http
  GET /author/me/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Auth Token for authenticating the user (Passed in header) |

#### Get List of Books (In Paginated Form)

```http
  GET /books/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Auth Token for authenticating the user (Passed in header) |

#### Get Current Author Info

```http
  GET /books/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Auth Token for authenticating the user (Passed in header) |
| `id` | `integer` | id of given book |

#### Like a Book

```http
  GET /books/like/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Auth Token for authenticating the user (Passed in header) |
| `id` | `integer` | **Required**. id of given book |

#### Unlike a book

```http
  GET /books/unlike/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Auth Token for authenticating the user (Passed in header) |
| `id` | `integer` | **Required**. id of given book |
