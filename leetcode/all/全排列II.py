class Solution:
    # nums duplicates
    def permuteUnique(self, nums):
        length = len(nums)
        if length == 0:
            return []
        if length == 1:
            return [nums]
        nums.sort()
        ans = []
        preciousNum = None
        for i in range(length):
            if nums[i] == preciousNum:
                continue
            preciousNum = nums[i]
            for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                ans.append([nums[i]]+j)
        return ans

r = Solution()
print(r.permuteUnique([1,1,2]))