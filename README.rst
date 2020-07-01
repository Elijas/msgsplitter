message-splitter
================

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


Splits long message to multiple messages in order to fit within an arbitrary message length limit (useful for SMS, Twitter, etc.).


Installation
------------
.. sourcecode:: bash

   ~ $ pip install msgsplitter

or you can install local version

.. sourcecode:: bash

   ~ $ pip install -e .

Quick start
-----------

.. sourcecode:: python

   >>> import msgsplitter
   >>> result = msgsplitter.split("Hello, this is a really long message.", length_limit=30)
   >>> result
   ['Hello, this is a really (1/2)', 'long message. (2/2)']

Run tests
-----------

.. sourcecode:: bash

   $ pytest
