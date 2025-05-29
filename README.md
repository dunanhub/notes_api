# 📝 FastAPI Notes API

> Асинхронный REST API для создания и получения текстовых заметок.  
> Разработан с использованием **FastAPI**, **PostgreSQL** и **SQLModel**.

---

## 🚀 Возможности

✅ Создание заметок  
✅ Получение всех заметок  
✅ Асинхронное взаимодействие с базой PostgreSQL  
✅ Простое тестирование через Postman

---

## 🧰 Стек технологий

- 🌐 [FastAPI](https://fastapi.tiangolo.com/)
- 🐘 [PostgreSQL](https://www.postgresql.org/)
- 🔄 [SQLModel](https://sqlmodel.tiangolo.com/)
- ⚡ [Uvicorn](https://www.uvicorn.org/)
- 🧠 [Pydantic](https://docs.pydantic.dev/)
- 📦 [asyncpg](https://magicstack.github.io/asyncpg/)

---

## 🛠️ Установка и запуск

```bash
# 📁 Клонируй репозиторий
git clone https://github.com/your-username/notes_api.git
cd notes_api
```

```bash
# 🧪 Создай виртуальное окружение

# Для Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Для Windows
python -m venv venv
venv\Scripts\activate
```

```bash
# 📦 Установи зависимости
pip install -r requirements.txt
```

```env
# ⚙️ Настрой файл .env
DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/notes_db
```

> 💡 Убедись, что база данных `notes_db` существует в PostgreSQL и PostgreSQL-сервер запущен.

```bash
# 🚀 Запусти FastAPI приложение
uvicorn app.main:app --reload
```

---

## 📬 Примеры API-запросов

### ➕ POST `/notes` — создать заметку

```http
POST http://localhost:8000/notes
```

```json
{
  "text": "Моя первая заметка"
}
```

### 📥 GET `/notes` — получить все заметки

```http
GET http://localhost:8000/notes
```

```json
[
  {
    "id": 1,
    "text": "Моя первая заметка",
    "created_at": "2025-05-30T10:00:00.000Z"
  }
]
```

---

## 🧪 Тестирование в Postman

1. Открой Postman
2. Отправь `POST` на `http://localhost:8000/notes` с JSON:
   ```json
   { "text": "Пример заметки" }
   ```
3. Отправь `GET` на `http://localhost:8000/notes` — должна вернуться твоя заметка.

---

## 📂 Структура проекта

```
notes_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes.py
├── .env
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚖️ Лицензия

Этот проект лицензирован под MIT. См. файл [LICENSE](./LICENSE) для подробностей.
