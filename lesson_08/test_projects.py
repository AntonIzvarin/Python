import pytest
from api_client import YougileProjectsClient


# --- НАСТРОЙКИ КОНФИГУРАЦИИ ---
BASE_URL = "https://yougile.com"
TOKEN = "Вставить_свой_API_KEY"
# ------------------------------


@pytest.fixture(scope="session")
def api():
    """Инициализация клиента API для всей тестовой сессии"""
    return YougileProjectsClient(base_url=BASE_URL, token=TOKEN)


@pytest.fixture
def temporary_project(api):
    """Фикстура для создания временного проекта (по аналогии с конспектом)"""
    payload = {
        "title": "Тестовый проект для проверок"
    }
    response = api.create_project(payload)
    assert response.status_code == 201, (
        "Не удалось создать предтребуемый проект для теста"
    )

    project_data = response.json()
    project_id = project_data.get("id")

    yield project_id


# ТЕСТЫ ДЛЯ МЕТОДА: [POST] /api-v2/projects

def test_create_project_positive(api):
    """Позитивный тест: Создание проекта с валидными данными"""
    payload = {
        "title": "Новый проект базовый"
    }
    response = api.create_project(payload)

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_missing_title(api):
    """Негативный тест: Попытка создать проект без обязательного поля"""
    payload = {}  # Пустой body без названия
    response = api.create_project(payload)

    assert response.status_code == 400


# ТЕСТЫ ДЛЯ МЕТОДА: [GET] /api-v2/projects/{id}

def test_get_project_positive(api, temporary_project):
    """Позитивный тест: Получение существующего проекта по ID"""
    response = api.get_project(temporary_project)

    assert response.status_code == 200
    assert response.json()["id"] == temporary_project


def test_get_project_negative_invalid_id(api):
    """Негативный тест: Попытка получить несуществующий проект"""
    non_existent_id = "99999999-9999-9999-9999-999999999999"
    response = api.get_project(non_existent_id)

    assert response.status_code == 404


# ТЕСТЫ ДЛЯ МЕТОДА: [PUT] /api-v2/projects/{id}

def test_update_project_positive(api, temporary_project):
    """Позитивный тест: Обновление названия существующего проекта"""
    updated_title = "Обновленное название проекта"
    payload = {
        "title": updated_title
    }
    response = api.update_project(temporary_project, payload)

    assert response.status_code == 200

    get_res = api.get_project(temporary_project)
    assert get_res.json()["title"] == updated_title


def test_update_project_negative_non_existent_id(api):
    """Негативный тест: Изменение проекта с несуществующим ID"""
    non_existent_id = "99999999-9999-9999-9999-999999999999"
    payload = {
        "title": "Новый заголовок"
    }
    response = api.update_project(non_existent_id, payload)

    assert response.status_code == 404
