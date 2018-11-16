#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

import mock
from mock import MagicMock

import to_test


class ToTestTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 如果 patch 多个外部函数，那么调用遵循自下而上的规则
    @mock.patch('to_test.mul')
    @mock.patch('to_test.add')
    def test_call_other_funcs_01(self, mock_add, mock_mul):
        x, y, a, b = 1, 2, 3, 4
        mock_add.return_value = 3
        mock_mul.return_value = 12
        result = to_test.call_other_funcs(x, y, a, b)
        # mock_add 确保调用过一次，如果没调用或多于一次，则抛出 AssertionError 异常
        mock_add.assert_called_once()
        mock_mul.assert_called_once()
        print result
        assert result is not None
        assert result == (3, 12)

    """
    simulate IOError
    side_effect function:
        1. set Exception
        2. set multi value for mock_func or mock_variant which multi called 
    """

    @mock.patch.object(to_test, 'mul', MagicMock(side_effect=IOError("io error!")))
    def test_call_other_funcs_02(self):
        result = to_test.call_other_funcs(1, 2, 3, 4)
        self.assertIsNone(result)

    # mock variant
    @mock.patch.object(to_test, 'global_variable', MagicMock(return_value='mock'))
    def test_call_other_funcs_03(self):
        to_test.call_other_funcs(1, 2, 3, 4)

    @mock.patch.object(to_test, 'add', MagicMock(return_value=None))
    def test_call_other_funcs_04(self):
        to_test.call_other_funcs(1, 2, 3, 4)

    @mock.patch.object(to_test, 'mul', MagicMock(return_value=None))
    def test_call_other_funcs_05(self):
        to_test.call_other_funcs(1, 2, 3, 4)


if __name__ == "__main__":
    unittest.main()
