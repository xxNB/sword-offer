# -*- coding: utf-8 -*-

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
        return even_number+odd_number

I = Solution()
print I.reorderarray([1,2,3,4,5,6,7])