


class Solution:
    def median(self, nums):
        nums.sort()
        return nums[(len(nums) - 1) / 2]
