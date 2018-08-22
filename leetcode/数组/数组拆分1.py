class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ix =0
        sum =0
        for i in nums:
            if ix %2==0:
                sum+=i
            ix+=1
        return sum


c = Solution()
print(c.arrayPairSum([1,4,3,2]))