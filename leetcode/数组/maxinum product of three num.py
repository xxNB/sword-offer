class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sorted(nums)
        p = nums[0]*nums[1]*nums[n-1]
        return max(p, nums[n-1]*nums[n-2]*nums[n-3])