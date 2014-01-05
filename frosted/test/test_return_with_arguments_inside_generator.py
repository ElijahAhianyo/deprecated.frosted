
from __future__ import absolute_import, division, print_function, unicode_literals

from sys import version_info

import pytest
from pies.overrides import *

from frosted import messages as m
from frosted.test.harness import TestCase

from .utils import flakes


@pytest.mark.skipif("version_info >= (3,)")
def test_return():
    flakes('''
    class a:
        def b():
            for x in a.c:
                if x:
                    yield x
            return a
    ''', m.ReturnWithArgsInsideGenerator)


@pytest.mark.skipif("version_info >= (3,)")
def test_returnNone():
    flakes('''
    def a():
        yield 12
        return None
    ''', m.ReturnWithArgsInsideGenerator)


@pytest.mark.skipif("version_info >= (3,)")
def test_returnYieldExpression():
    flakes('''
    def a():
        b = yield a
        return b
    ''', m.ReturnWithArgsInsideGenerator)