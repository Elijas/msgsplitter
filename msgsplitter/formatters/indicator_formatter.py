from msgsplitter.exceptions import LengthLimitTooLowError
from msgsplitter.formatters.formatter_base import FormatterBase, RecalculateGroups


class IndicatorFormatter(FormatterBase):
    def __init__(self, length_limit: int, total_count_digits=0):
        """
        >>> IndicatorFormatter(7, 1)  #doctest: +ELLIPSIS
        <...IndicatorFormatter object at ...>
        >>> IndicatorFormatter(6, 1)
        Traceback (most recent call last):
        ...
        msgsplitter.exceptions.LengthLimitTooLowError
        """
        super().__init__(length_limit)
        if total_count_digits and self._length_limit - len(f' (/)') - 2 * total_count_digits < 1:
            raise LengthLimitTooLowError
        self._total_count_digits = total_count_digits

    def is_message_too_long(self, message_length: int, message_idx: int):
        """
        >>> IndicatorFormatter(5).is_message_too_long(5, 1)
        False
        >>> IndicatorFormatter(5).is_message_too_long(5, 2)
        Traceback (most recent call last):
        ...
        msgsplitter.exceptions.LengthLimitTooLowError
        >>> IndicatorFormatter(10).is_message_too_long(5, 2)
        Traceback (most recent call last):
        ...
        msgsplitter.formatters.formatter_base.RecalculateGroups
        >>> IndicatorFormatter(10, 1).is_message_too_long(5, 2)
        True
        >>> IndicatorFormatter(11, 1).is_message_too_long(5, 2)
        False
        """
        if (0 < self._total_count_digits < len(str(message_idx))
                or self._total_count_digits == 0 and message_idx > 1):
            new_formatter = IndicatorFormatter(self._length_limit, len(str(message_idx)))
            raise RecalculateGroups(new_formatter=new_formatter)
        if self._total_count_digits == 0:
            return message_length > self._length_limit
        else:
            return message_length > self._length_limit - len(f' (/)') - len(str(message_idx)) - self._total_count_digits

    def format(self, split_messages):
        """
        >>> IndicatorFormatter(10, 1).format(['A', 'B', 'C'])
        ['A (1/3)', 'B (2/3)', 'C (3/3)']
        """
        if self._total_count_digits == 0:
            return super().format(split_messages)
        return super().format([f'{message} ({i}/{len(split_messages)})'
                               for i, message in enumerate(split_messages, start=1)])
