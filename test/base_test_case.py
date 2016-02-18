# coding: utf-8

from __future__ import absolute_import, unicode_literals

import six

TestCase = None  # pylint:disable=invalid-name

# pylint:disable=wrong-import-position,wrong-import-order
try:
    from unittest import skipIf, TestCase  # pylint:disable=unused-import
except ImportError:
    if not hasattr(TestCase, 'assertItemsEqual') and not hasattr(TestCase, 'assertCountEqual'):
        # Python 2.6 support
        # pylint:disable=import-error
        from unittest2 import skipIf, TestCase
        # pylint:enable=import-error
# pylint:enable=wrong-import-position,wrong-import-order

if six.PY3:
    # pylint:disable=no-member,maybe-no-member
    TestCase.assertItemsEqual = TestCase.assertCountEqual
