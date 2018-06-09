"""

508. Wiggle Sort
Given an unsorted array nums, reorder it in-place such that

nums[0] <= nums[1] >= nums[2] <= nums[3]....
Example
Given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
"""


class Solution:
    """
    摇摆排序
    @param: nums: A list of integers
    @return: nothing
    """

    def wiggleSort(self, nums):
        # write your code here
        for i in range(1, int(len(nums))-1):
            print(i)
            if i % 2 == 1 and nums[i] < nums[i + 1] or i % 2 == 0 and nums[i] > nums[i - 1]:
                tmp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = tmp
        print(nums)

c = Solution()
c.wiggleSort([3, 5, 2, 1, 6, 4])
