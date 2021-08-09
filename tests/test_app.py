import pytest

MOCK_DICTIONARY = {
    "first_name": "Leopoldo"
    "last_name": "Flores"
    "active": 1,
    "age": 19
    "username": "Leo"
}

def test_dictionary_has_valid_age():
    assert isinstance(MOCK_DICTIONARY["age"], int)

def test_dictionary_has_valid_username():
    assert MOCK_DICTIONARY.get("username") == "LeopoldoFlores"


