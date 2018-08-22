class Solution:
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            if 0 < nums[i] and nums[i] < len(nums):
                while nums[i] != i + 1:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                    if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == nums[nums[i] - 1]:
                        break

        jet = 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                jet = 0
                ans = i + 1
                break

        if jet == 1:
            ans = len(nums) + 1
        return ans
