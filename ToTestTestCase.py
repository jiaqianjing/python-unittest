#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import mock

import to_test


class ToTestTestCase(unittest.TestCase):
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
        print result
        assert result is not None
        assert result == (3, 12)


if __name__ == "__main__":
    unittest.main()
