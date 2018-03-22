# -*- coding: utf-8 -*-

# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return []
        new_array = self.quicksort(tinput)
        return new_array[:k]

    def quicksort(self, array):
        # 申请写一个快排
        if len(array) < 2:
            return array
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return self.quicksort(less) + [pivot] + self.quicksort(greater)


I = Solution()
print(I.GetLeastNumbers_Solution(tinput=[4, 5, 1, 6, 2, 7, 3, 8], k=10))
