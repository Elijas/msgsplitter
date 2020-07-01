from dataclasses import dataclass


class FormatterBase:
    def __init__(self, length_limit: int):
        self._length_limit = length_limit

    def is_message_too_long(self, message_length: int, message_idx: int):
        return message_length > self._length_limit

    def format(self, split_messages):
        for message in split_messages:
            assert len(message) <= self._length_limit
        return split_messages


@dataclass
class RecalculateGroups(Exception):
    new_formatter: FormatterBase
