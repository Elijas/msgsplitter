message-splitter
================

.. role:: python(code)
   :language: python
.. image:: https://img.shields.io/travis/com/Elijas/msgsplitter.svg
   :target: https://travis-ci.com/elijas/msgsplitter
.. image:: https://img.shields.io/pypi/v/msgsplitter.svg
   :target: https://pypi.org/project/msgsplitter/
.. image:: https://img.shields.io/pypi/pyversions/msgsplitter.svg
   :target: https://pypi.org/project/msgsplitter/
.. image:: https://img.shields.io/github/issues/Elijas/msgsplitter.svg
   :target: https://github.com/Elijas/msgsplitter/issues
.. image:: https://img.shields.io/github/license/elijas/msgsplitter.svg
   :target: https://github.com/Elijas/msgsplitter/blob/master/LICENSE


Splits a long piece of text (messages) to multiple text strings (messages) in order to fit within an arbitrary message length limit (useful for SMS, Twitter, etc.).

Whitespace is used as the breaking point for splitting messages. All whitespace in the text is replaced with a single space.

Installation
------------
.. sourcecode:: bash

   ~ $ pip install msgsplitter

or you can install a local development version after cloning the project:

.. sourcecode:: bash

   ~ $ pip install -e .

Quick start
-----------
.. sourcecode:: python

   >>> import msgsplitter
   >>> msg = 'Hello, this is a really long message.'
   
   >>> msgsplitter.split(msg, length_limit=30)
   ['Hello, this is a really (1/2)', 'long message. (2/2)']
   
   >>> msgsplitter.split(msg, length_limit=30, append_indicator=False)
   ['Hello, this is a really long', 'message.']

Formatting extensibility
-----------
You can create custom formatting classes. Your class will define, how many characters must be reserved in each message for adding the formatting characters after the content split into chunks is made. You can take a look at the two example classes for inspiration: :python:`FormatterBase`, which is identical to just using the :python:`split(...)` with the argument :python:`append_indicator=False`, and the other class :python:`IndicatorFormatter`, which is identical to just using :python:`split(...)` with the argument :python:`append_indicator=True`.

Custom class is passed through the :python:`formatter_cls` argument and overrides the :python:`append_indicator` setting. Usage example:

.. sourcecode:: python

   msgsplitter.split('some text', 10, formatter_cls=IndicatorFormatter)


Run tests
-----------

.. sourcecode:: bash

   ~ $ pytest
