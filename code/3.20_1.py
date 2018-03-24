# -*- coding: utf-8 -*-

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，
# 偶数和偶数之间的相对位置不变

class Solution:
    def reorderarray(self, array):
        # write code here
        odd_number = []
        even_number = []
        for item in array:
            if item % 2 == 0:
                print item
                odd_number.append(item)
            else:
                even_number.append(item)
        return even_number + odd_number


I = Solution()
print I.reorderarray([1, 2, 3, 4, 5, 6, 7])
