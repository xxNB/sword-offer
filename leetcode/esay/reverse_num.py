"""
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
"""


class Solution:
    def reverse(self, x):
        """

        :type x: int
        :rtype: int
        """
        if not -2**31 < x < 2**31-1:
            return 0
        pos = True
        if x < 0:
            pos = False
            x = -x
        t = 0
        while x != 0:
            # % 余数 // 取商
            t = t * 10 + x % 10
            x //= 10
        if not pos:
            return -t
        if not -2**31 < t < 2**31-1:
            return 0
        return t


r = Solution()
print(r.reverse(-2147483648))
