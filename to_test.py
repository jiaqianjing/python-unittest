#!/usr/bin/env python
# -*- coding: utf-8 -*-

# to_test.py

global_variable = "TEST"

def add(x, y):
    ret = x + y
    return ret


def mul(a, b):
    ret = a * b
    return ret


def call_other_funcs(x, y, a, b):
    try:
        demo = "demo"
        ret01 = add(x, y)
        ret02 = mul(a, b)
        print "global_variable: {}".format(global_variable)
        print "demo: {} ret01: {} ret02: {}".format(demo, ret01, ret02)

        # 对得到的 ret01, ret02 进行一些处理，得到最终返回值 ret。例如
        if ret01 and ret02:
            ret = (ret01, ret02)
        elif ret01 and (not ret02):
            ret = (ret01, 0)
        elif (not ret01) and ret02:
            ret = (0, ret02)
        else:
            ret = (0, 0)
        return ret
    except Exception as e:
        print "error: {}".format(e)


if __name__ == "__main__":
    result = call_other_funcs(1, 2, 3, 4)
    print result, global_variable
