# RefLink

## Описание
RefLink — это API-сервис для реферальной системы, позволяющий пользователям создавать и управлять реферальными кодами, регистрироваться по коду, а также получать информацию о своих рефералах.


## Функциональные возможности

- Регистрация и аутентификация пользователей (JWT, OAuth 2.0)
- Создание и удаление реферального кода (может быть активен только один код с заданным сроком годности)
- Получение реферального кода по email
- Регистрация по реферальному коду
- Получение информации о рефералах
- UI-документация API (Swagger/ReDoc)

## Как начать работу с проектом?

### 1.Клонируйте репозиторий:
```bash
git clone git@github.com:Cubaser/reflink.git
cd reflink
```

### 2. Установка виртуального окружения и зависимостей
Активируйте виртуальное окружение и установите необходимые библиотеки:
```bash
python3 -m venv venv
source venv/bin/activate # для Linux
source venv/scripts/activate # для Windows
pip install -r requirements.txt
```

### 3. Настройка переменных окружения
Создайте в корне проекта файл `.env` со следующим содержимым:
```env
APP_TITLE=REFLINK
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET_KEY=<ваш_секретный_ключ>
DOMAIN=<домен>
```

Примените миграции базы данных:
```bash
alembic upgrade head
```

Запустите сервер:
```bash
uvicorn app.main:app
```

Проект станет доступен по адресу: [RefLink](http://127.0.0.1:8000).

### Основные технологии:
- **Python**
- **Fastapi**
- **SQLAlchemy**

### Документация
Документация к API доступна по следующим адресам:

- [Swagger UI](http://127.0.0.1:8000/docs) — документация API.
- [Redoc](http://127.0.0.1:8000/redoc) — альтернативная документация API.

---

## Автор
Иванов Виктор
[cubaser@mail.ru](mailto:cubaser@mail.ru)

