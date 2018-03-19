# -*- coding: utf-8 -*-

# 输入一个整数n, 请你输出斐波那契数列的第n项

class Solution:
    def Fibonacci(self, n):
        a, b = 0, 1
        while n > 0:
            a, b = b, a+b
            n -= 1
        return a


