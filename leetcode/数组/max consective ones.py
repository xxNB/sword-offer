class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curcnt = 0
        sums = 0
        # f = nums[0]
        for i in range(0, len(nums)):
            if nums[i] ==1:
                curcnt+=1
                sums = max(sums, curcnt)
            else:
                curcnt = 0
        return sums

c = Solution()
print(c.findMaxConsecutiveOnes([1,1,0,1,]))