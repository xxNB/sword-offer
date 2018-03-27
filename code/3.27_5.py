# -*- coding: utf-8 -*-

# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        still = []
        for ix, i in enumerate(array):
            item = array.pop(ix)
            if i not in array:
                still.append(i)
            array.insert(ix, item)
        return still


c = Solution()
print c.FindNumsAppearOnce([2, 2, 3, 3, 4, 4, 5, 6])
