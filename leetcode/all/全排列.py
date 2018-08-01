class Solution:

    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        ans = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for y in self.permute(n):
                ans.append([num] + y)
        return ans

r = Solution()
print(r.permute([1,2,3]))