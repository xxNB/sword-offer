# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。


class Solution:
    def isPalidrome(self, x):
        """

        :type x:  int
        :rtype: bool
        """
        new_x = "".join(reversed(str(x)))
        if new_x == str(x):
            return True
        return False


c = Solution()
print(c.isPalidrome(121))
