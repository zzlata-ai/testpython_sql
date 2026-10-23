import os
import psycopg
import pytest

HOST = "localhost"
PORT = 5433
DBNAME = "testdb"
USER = "postgres"
# пароль можно подменить через переменную окружения, чтобы проверить неудачный вход
PASSWORD = os.environ.get("PG_PASSWORD", "secret123")


@pytest.fixture
def conn():
    c = psycopg.connect(host=HOST, port=PORT, dbname=DBNAME,
                        user=USER, password=PASSWORD, connect_timeout=5)
    yield c
    c.close()


def test_connect(conn):
    assert conn.closed == 0


def test_select_now(conn):
    cur = conn.cursor()
    cur.execute("select now()")
    result = cur.fetchone()
    cur.close()
    assert result is not None
    assert result[0] is not None
