class Solution:
    def majorityElement(self,nums):
        res, cnt = 0, 0
        for num in nums:
            if cnt ==0:
                res = num
                cnt+=1
            elif num == res:
                cnt+=1
            else:
                cnt-=1
        return res