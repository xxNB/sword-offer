class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if target in nums:
        #     return nums.index(target)
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (j - i) // 2 + i
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return i if nums[i] > target else i + 1


c= Solution()
print(c.searchInsert([1,3,5,6], 7))