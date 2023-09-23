import pytest

from src.item import Item
from src.keyboard import Keyboard
from settings import KEYBOARD

@pytest.fixture
def kb():
    """Создаем экземпляр класса в фикстуре"""
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_str(kb):
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_change_lang(kb):
    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    assert str(kb.language) == "EN"

