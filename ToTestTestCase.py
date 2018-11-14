#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import mock

import to_test


class ToTestTestCase(unittest.TestCase):
    @mock.patch('to_test.add')
    @mock.patch('to_test.mul')
    def test_call_other_funcs(self, mock_add, mock_mul):
        x = 1
        y = 2
        a = 3
        b = 4
        mock_add.return_value = 3
        mock_mul.return_value = 12
        result = to_test.call_other_funcs(x, y, a, b)
        print mock_add, mock_mul
        print result
        self.assertIsNotNone(result, (12, 3))


if __name__ == "__main__":
    unittest.main()
