from typing import Callable

from msgsplitter._split_message import split_message
from msgsplitter.formatters.formatter_base import FormatterBase, RecalculateGroups
from msgsplitter.formatters.indicator_formatter import IndicatorFormatter


def _get_split_messages(message, formatter):
    while True:
        try:
            return split_message(message, formatter), formatter
        except RecalculateGroups as e:
            formatter = e.new_formatter


def split(message: str, length_limit: int,
          formatter_cls: Callable[[int], FormatterBase] = IndicatorFormatter):
    formatter = formatter_cls(length_limit)
    split_messages, formatter = _get_split_messages(message, formatter)
    return formatter.format(split_messages)


if __name__ == '__main__':
    print(split('Hello, this is a really long message.', length_limit=30))
