# -*- coding: utf-8 -*-

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

class Solution:
    def jumpfloorii(self, number):
        if number <= 0:
            val = 0
        elif number == 1:
            val = 1
        elif number == 2:
            val = 2
        else:
            val = 2
            for i in range(3, number+1):
                val = 2*val
        return val
