from typing import Callable

from msgsplitter._split_message import split_message
from msgsplitter.formatters.formatter_base import FormatterBase, RecalculateGroups
from msgsplitter.formatters.indicator_formatter import IndicatorFormatter


def _get_split_messages(message, formatter):
    """
    Split content into chunks that will still leave space for extra formatting characters.

    May construct a different formatter from the given one, if messages can't fit with the current one
    (it's done so that internal state of the formatter variables wouldn't be changed,
     for concurrency considerations, etc.)
    """
    while True:
        try:
            return split_message(message, formatter), formatter
        except RecalculateGroups as e:
            formatter = e.new_formatter


def split(message: str, length_limit: int,
          append_indicator: bool = True,
          formatter_cls: Callable[[int], FormatterBase] = None):
    """
    Splits text string into chunks no longer than length_limit.
    Formatting is controlled through append_indicator=[True|False] or a custom formatter_cls class.
    """
    assert length_limit > 0, 'length_limit must be a positive integer'
    if formatter_cls is None:
        if append_indicator:
            formatter_cls = IndicatorFormatter
        else:
            formatter_cls = FormatterBase

    formatter = formatter_cls(length_limit)
    # Split content into chunks that will still leave space for extra formatting characters
    split_messages, new_formatter = _get_split_messages(message, formatter)
    # Add the extra formatting characters
    return new_formatter.format(split_messages)


if __name__ == '__main__':
    print(split('Hello, this is a really long message.', length_limit=30))
    print(split('Hello, this is a really long message.', length_limit=30, append_indicator=False))
