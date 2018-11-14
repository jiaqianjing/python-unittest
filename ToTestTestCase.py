#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

import mock

import to_test


class ToTestTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 如果 patch 多个外部函数，那么调用遵循自下而上的规则
    @mock.patch('to_test.mul')
    @mock.patch('to_test.add')
    def test_call_other_funcs(self, mock_add, mock_mul):
        x = 1
        y = 2
        a = 3
        b = 4
        mock_add.return_value = 3
        mock_mul.return_value = 12
        result = to_test.call_other_funcs(x, y, a, b)
        # mock_add 确保调用过一次，如果没调用或多于一次，则抛出 AssertionError 异常
        mock_add.assert_called_once()
        mock_mul.assert_called_once()
        print result
        assert result is not None
        assert result == (3, 12)


if __name__ == "__main__":
    unittest.main()
