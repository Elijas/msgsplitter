message-splitter
================


.. image:: https://img.shields.io/travis/elijas/msgsplitter
   :target: https://travis-ci.org/elijas/msgsplitter
.. image:: https://img.shields.io/github/license/elijas/msgsplitter
   :target: https://github.com/elijas/msgsplitter


Splits long message to multiple messages in order to fit within an arbitrary message length limit (useful for SMS, Twitter, etc.).

Quick start
-----------

Code example:

.. sourcecode:: python

   >>> import msgsplitter
   >>> result = msgsplitter.split("Hello, this is a really long message.", 30)
   >>> result
   ['Hello, this is a really (1/2)', 'long message. (2/2)']

Run tests:

.. sourcecode:: bash

   $ pytest --doctest-modules