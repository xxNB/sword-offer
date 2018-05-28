"""

373. Partition Array by Odd and Even
Partition an integers array into odd number first and even number second.

Example
Given [1, 2, 3, 4], return [1, 3, 2, 4]

Challenge
Do it in-place.
"""

class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """

    def partitionArray(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        while start < end:
            while start < end and nums[start] % 2 == 1:
                # print(start, end)
                start += 1
            while start < end and nums[end] % 2 == 0:
                # print(start, end)
                end -= 1
            if start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1


c = Solution()
c.partitionArray([2147483644, 2147483645, 2147483646, 2147483647])
