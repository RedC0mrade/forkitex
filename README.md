# Tron Wallet Info Microservice
Микросервис на FastAPI который выводит информацию по адресу в сети трон, его bandwidth, energy, и баланс trx. Поддерживает асинхронную работу, использует SQLAlchemy, Pydantic, TronPy и SQLite/PostgreSQL.

---

## Функциональность
- Получение информации о Tron-адресе:

 - Баланс (TRX)

 - Энергия

 - Пропускная способность

- Сохранение запроса в БД

- Получение истории запросов с пагинацией

---

## Стек технологий
- Python 3.13.1

- **FastAPI**

- **SQLAlchemy (async)**

- **Pydantic**

- **TronPy**

- **Starlette**

- **SQLite / PostgreSQL**

- **Alembic (для миграций)**

- **Pytest (для тестирования)**

---

## Установка

```bash
git clone git@github.com:RedC0mrade/forkitex.git
cd forkitex
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
docker-compose up --build -d
uvicorn app.main:main_app --reload
```

## Переменные окружения
Создайте файл .env (или используйте .env.example)

## Эндпоинты
 - POST /forkytech/tron/wallet_info
   - Пример запроса:
    {
        "address": "TXYZ1234567890"
    }
  -  Пример ответа:
    {
        "address": "TXYZ1234567890",
        "balance": 123.45,
        "bandwidth": 5000,
        "energy": 10000
    }
 - GET /forkytech/tron/requests?skip=0&limit=10
   - Пример ответа:
    [
        {
            "id": 1,
            "address": "TXYZ1234567890",
            "timestamp": 1713700000
        }
    ]