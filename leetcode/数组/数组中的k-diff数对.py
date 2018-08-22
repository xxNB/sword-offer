class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        双指针解法
        """
        res,n = 0, len(nums)
        m = dict()
        for num in nums:
            if num not in m:
                m[num]= 0
            m[num]+=1
        for item in m.items():
            if k ==0 and item[1]>1:
                res+=1
            elif k>0 and (item[0]+k) in m.keys():
                res+=1
        return res

c = Solution()
print(c.findPairs([3,1,4,1,5],2))
