# -*- coding: utf-8 -*-

# 把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个
# 丑数。求按从小到大的顺序的第N个丑数。

class Solution:
    def GetUglyNumber_Solution(self, index):
        if (index <= 0):
            return 0
        uglyList = [1]
        indexTwo = 0
        indexThree = 0
        indexFive = 0
        for i in range(index - 1):
            newUgly = min(uglyList[indexTwo] * 2, uglyList[indexThree] * 3, uglyList[indexFive] * 5)
            print newUgly
            uglyList.append(newUgly)
            if (newUgly % 2 == 0):
                indexTwo += 1
            if (newUgly % 3 == 0):
                indexThree += 1
            if (newUgly % 5 == 0):
                indexFive += 1
            print i, indexTwo, indexThree, indexFive
        return uglyList[-1]


c = Solution()
print c.GetUglyNumber_Solution(10)
