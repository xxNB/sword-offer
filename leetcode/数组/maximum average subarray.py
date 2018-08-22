class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        re = sum(nums[:k])
        sums = re
        n = len(nums)
        for i in range(k, n):
            sums = sums -nums[i-k]+nums[i]
            re = max(sums, re)
        return re / k


c = Solution()
print(c.findMaxAverage([0,4,0,3,2], 1))