import pytest

from msgsplitter.formatters.formatter_base import FormatterBase
from msgsplitter.formatters.indicator_formatter import IndicatorFormatter
from msgsplitter.split import split


@pytest.mark.parametrize('formatter', [FormatterBase, IndicatorFormatter])
def test_given_one_word__when_split__then_returns_one_message(formatter):
    message = 'Hi'

    messages = split(message, 2, formatter)

    assert messages == [message]


@pytest.mark.parametrize('formatter', [FormatterBase, IndicatorFormatter])
def test_given_multiple_words__when_split__then_returns_dynamically_sized_messages(formatter):
    message = 'A ' * 26

    messages = split(message, 10, formatter)

    if formatter is FormatterBase:
        expected = ['A A A A A', 'A A A A A', 'A A A A A', 'A A A A A', 'A A A A A', 'A']
    else:
        expected = ['A A (1/17)', 'A A (2/17)', 'A A (3/17)', 'A A (4/17)', 'A A (5/17)',
                    'A A (6/17)', 'A A (7/17)', 'A A (8/17)', 'A A (9/17)',
                    'A (10/17)', 'A (11/17)', 'A (12/17)', 'A (13/17)',
                    'A (14/17)', 'A (15/17)', 'A (16/17)', 'A (17/17)']
    assert messages == expected
