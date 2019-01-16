class Solution:
    """
    给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
    你找到的子数组应是最短的，请输出它的长度。
    """
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
