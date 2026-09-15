import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА capitalize
# =====================================================================

# Позитивные тесты (строки с буквами, где ожидается изменение регистра)
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("hello", "Hello"),
    ],
)
def test_capitalize_positive(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


# Негативные тесты и граничные условия
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("123hello", "123hello"),
        ("04 апреля 2023", "04 апреля 2023"),
        ("", ""),
        (" ", " "),
    ],
)
def test_capitalize_negative_and_boundary(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


def test_capitalize_negative_none(utils):
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА trim
# =====================================================================

# Позитивные тесты (удаление пробелов в начале)
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("  04 апреля 2023", "04 апреля 2023"),
    ],
)
def test_trim_positive(utils, input_str, expected):
    assert utils.trim(input_str) == expected


# Негативные тесты и граничные условия (строки без пробелов, пустые)
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("04 апреля 2023", "04 апреля 2023"),
        ("", ""),
    ],
)
def test_trim_negative_and_boundary(utils, input_str, expected):
    assert utils.trim(input_str) == expected


# ВНИМАНИЕ: Тест вызывает БЕСКОНЕЧНЫЙ ЦИКЛ (BUG-001)
# Перенесен в негативные, так как строка состоит только из пробелов
# def test_trim_spaces_only_negative(utils):
#     assert utils.trim(" ") == ""


def test_trim_negative_none(utils):
    with pytest.raises(AttributeError):
        utils.trim(None)


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА contains
# =====================================================================

# Позитивные тесты (поиск присутствующих символов/подстрок)
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "P", True),
        ("123", "2", True),
        ("04 апреля 2023", "апреля", True),
        (" ", " ", True),
    ],
)
def test_contains_positive(utils, input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected


# Негативные тесты и граничные условия
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "X", False),
        ("", "S", False),
    ],
)
def test_contains_negative_and_boundary(utils, input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected


def test_contains_negative_none(utils):
    with pytest.raises(AttributeError):
        utils.contains(None, "S")


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА delete_symbol
# =====================================================================

# Позитивные тесты (удаление существующих подстрок)
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "Pro", "Sky"),
        ("123", "2", "13"),
        ("04 апреля 2023", " 2023", "04 апреля"),
    ],
)
def test_delete_symbol_positive(utils, input_str, symbol, expected):
    # Тест упадет из-за критической ошибки в коде метода (BUG-002)
    assert utils.delete_symbol(input_str, symbol) == expected


# Негативные тесты и граничные условия (удаление отсутствующих)
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        # удаление того, чего нет
        ("SkyPro", "NotFound", "SkyPro"),
        ("", "S", ""),
    ],
)
def test_delete_symbol_negative_and_boundary(
        utils, input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected


def test_delete_symbol_negative_none(utils):
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "S")
