class Solution:
    def findUnsortedSubarray(self, nums):
        sortedNum, length = sorted(nums), len(nums)
        start, end = 0, length - 1
        while start < length and sortedNum[start] == nums[start]:
            start += 1
        while end > start and sortedNum[end] == nums[end]:
            end -= 1
        return end - start + 1


c = Solution()
print(c.findUnsortedSubarray([1, 3, 2, 3, 3]))
