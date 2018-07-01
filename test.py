import pytest
from main import create_gen


def test_main():
    text = 'my name is Masha'
    expected = [2, 4, 2, 5]
    output = list(create_gen(text))

    assert output == expected