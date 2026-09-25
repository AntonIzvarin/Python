import pytest
from sqlalchemy import create_engine, text


DATABASE_URL = "postgresql://postgres:123123@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Фикстура модуля: создает таблицу перед всеми тестами
    и удаляет её после их завершения."""
    with engine.connect() as connection:
        with connection.begin():
            # Создаем таблицу students, если её нет
            connection.execute(
                text("""
                CREATE TABLE IF NOT EXISTS students (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL
                );
            """)
            )

    yield  # Здесь запускаются сами тесты

    with engine.connect() as connection:
        with connection.begin():
            # Полностью удаляем таблицу после окончания всех тестов
            connection.execute(text("DROP TABLE IF EXISTS students;"))


@pytest.fixture
def clean_up_student():
    """Фикстура для очистки конкретных тестовых записей после каждого теста."""
    yield
    with engine.connect() as connection:
        with connection.begin():
            connection.execute(
                text("DELETE FROM students WHERE name = 'Тестовый Студент'")
            )


# 1. ТЕСТ НА ДОБАВЛЕНИЕ
def test_create_student(clean_up_student):
    with engine.connect() as connection:
        with connection.begin():
            connection.execute(
                text("INSERT INTO students (name) VALUES ('Тестовый Студент')")
            )

        result = connection.execute(
            text("SELECT * FROM students WHERE name = 'Тестовый Студент'")
        ).fetchone()

        assert result is not None
        assert result.name == "Тестовый Студент"


# 2. ТЕСТ НА ИЗМЕНЕНИЕ
def test_update_student(clean_up_student):
    with engine.connect() as connection:
        with connection.begin():
            connection.execute(
                text("INSERT INTO students (name) VALUES ('Тестовый Студент')")
            )
            connection.execute(
                text(
                    "UPDATE students SET name = "
                    "'Новое Имя Студента' WHERE name = 'Тестовый Студент'"
                )
            )

        old_result = connection.execute(
            text("SELECT * FROM students WHERE name = 'Тестовый Студент'")
        ).fetchone()
        new_result = connection.execute(
            text("SELECT * FROM students WHERE name = 'Новое Имя Студента'")
        ).fetchone()

        assert old_result is None
        assert new_result is not None

        # Подчищаем измененное имя за собой
        with connection.begin():
            connection.execute(
                text("DELETE FROM students WHERE name = 'Новое Имя Студента'")
            )


# 3. ТЕСТ НА УДАЛЕНИЕ
def test_delete_student():
    with engine.connect() as connection:
        with connection.begin():
            connection.execute(
                text("INSERT INTO students (name) VALUES ('Тестовый Студент')")
            )
            connection.execute(
                text("DELETE FROM students WHERE name = 'Тестовый Студент'")
            )

        result = connection.execute(
            text("SELECT * FROM students WHERE name = 'Тестовый Студент'")
        ).fetchone()

        assert result is None
