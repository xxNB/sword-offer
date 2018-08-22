class Solution:
    def thirdMax(self, nums):
        """
        维持一个依次减小的数组res，保证每次遍历数组中的三个数都是最大的三个。

        :type nums: List[int]
        :rtype: int
        """
        res = [float("-inf")] * 3
        for i in nums:
            if i in res:
                continue
            if i > res[0]:
                res = [i, res[0], res[1]]
            elif i > res[1]:
                res = [res[0], i, res[1]]
            elif i > res[2]:
                res = [res[0], res[1], i]
            print(res)
        return res[-1] if res[2] != float("-inf") else res[0]


c = Solution()
print(c.thirdMax([2, 2, 3, 1]))