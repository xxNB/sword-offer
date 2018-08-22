
class Solution:
    def missingNumner(self,nums):
        """
        time: O(n)
        space: O(1)
        :param nums:
        :return:
        """
        i =0
        sums = 0
        while i<len(nums)+1:
            sums +=i
            i+=1
        return sums-sum(nums)

c = Solution()
print(c.missingNumner([3,0,1]))