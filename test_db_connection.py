import os

import psycopg
import pytest


def db_params():
    """Параметры подключения; можно переопределить переменными окружения."""
    return {
        "host": os.getenv("PG_HOST", "localhost"),
        "port": int(os.getenv("PG_PORT", "5433")),
        "dbname": os.getenv("PG_DB", "testdb"),
        "user": os.getenv("PG_USER", "postgres"),
        "password": os.getenv("PG_PASSWORD", "secret123"),
        "connect_timeout": 5,
    }


@pytest.fixture
def connection():
    with psycopg.connect(**db_params()) as conn:
        yield conn


def test_connection_is_open(connection):
    assert not connection.closed


def test_select_now(connection):
    with connection.cursor() as cur:
        cur.execute("select now()")
        row = cur.fetchone()

    assert row is not None
    assert row[0] is not None
