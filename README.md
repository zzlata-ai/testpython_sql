# Автотест подключения к PostgreSQL

Тест на Python (pytest + psycopg 3) проверяет, что к базе данных PostgreSQL
можно подключиться и что простейший запрос `select now()` возвращает результат.

## Что проверяется

- `test_connection_is_open` — соединение с БД установлено;
- `test_select_now` — запрос `select now()` выполняется и возвращает значение.

## Требования

- Python 3.9+
- Docker (для запуска PostgreSQL)

## Запуск

1. Поднять PostgreSQL в Docker:

   ```bash
   docker run -d --name pg-test \
     -e POSTGRES_PASSWORD=secret123 \
     -e POSTGRES_DB=testdb \
     -p 5433:5432 postgres:16
   ```

2. Создать виртуальное окружение и установить зависимости:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Запустить тесты:

   ```bash
   pytest -v test_db_connection.py
   ```

Ожидаемый результат: `2 passed`.

## Проверка с неверным паролем

Параметры подключения можно переопределить переменными окружения
(`PG_HOST`, `PG_PORT`, `PG_DB`, `PG_USER`, `PG_PASSWORD`).
Чтобы увидеть падение тестов, передайте неверный пароль:

```bash
PG_PASSWORD=wrong pytest -v test_db_connection.py
```

Тесты завершатся с ошибкой `psycopg.OperationalError: ... password authentication failed for user "postgres"`.

## Параметры по умолчанию

| Переменная    | Значение по умолчанию |
|---------------|-----------------------|
| `PG_HOST`     | `localhost`           |
| `PG_PORT`     | `5433`                |
| `PG_DB`       | `testdb`              |
| `PG_USER`     | `postgres`            |
| `PG_PASSWORD` | `secret123`           |

## Остановка БД

```bash
docker stop pg-test && docker rm pg-test
```
