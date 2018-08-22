class Solution:
    def threeSum(self, nums):
        nums.sort()
        count = len(nums)
        collect = []
        for i in range(count):
            left = i+1
            right = count -1
            if i > 0 and nums[i] == nums[i-1]:
                left+=1
                continue
            while left < right:
                sum = nums[i]+nums[left]+nums[right]
                if sum == 0:
                    col = [nums[i], nums[left], nums[right]]
                    collect.append(col)
                    left+=1
                    right-=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    while nums[right] == nums[right+1] and left<right:
                        right-=1
                if sum<0:
                    left+=1
                elif sum>0:
                    right-=1
        return collect

