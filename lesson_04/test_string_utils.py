import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА capitalize
# =====================================================================


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("123hello", "123hello"),
        ("04 апреля 2023", "04 апреля 2023"),
    ],
)
def test_capitalize_positive(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        (" ", " "),
    ],
)
def test_capitalize_boundary(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


def test_capitalize_none(utils):
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА trim
# =====================================================================


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("04 апреля 2023", "04 апреля 2023"),
    ],
)
def test_trim_positive(utils, input_str, expected):
    assert utils.trim(input_str) == expected


def test_trim_empty(utils):
    assert utils.trim("") == ""


# ВНИМАНИЕ: Тест вызывает БЕСКОНЕЧНЫЙ ЦИКЛ (BUG-001)
# def test_trim_spaces_only(utils):
#     assert utils.trim(" ") == ""


def test_trim_none(utils):
    with pytest.raises(AttributeError):
        utils.trim(None)


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА contains
# =====================================================================


@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "P", True),
        ("123", "2", True),
        ("04 апреля 2023", "апреля", True),
    ],
)
def test_contains_positive(utils, input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("", "S", False),
        (" ", " ", True),
    ],
)
def test_contains_boundary(utils, input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected


def test_contains_none(utils):
    with pytest.raises(AttributeError):
        utils.contains(None, "S")


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА delete_symbol
# =====================================================================


@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "Pro", "Sky"),
        ("123", "2", "13"),
        ("04 апреля 2023", " 2023", "04 апреля"),
    ],
)
def test_delete_symbol_positive(utils, input_str, symbol, expected):
    # Тест упадет из-за критической ошибки в коде метода (BUG-003)
    assert utils.delete_symbol(input_str, symbol) == expected


def test_delete_symbol_none(utils):
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "S")
