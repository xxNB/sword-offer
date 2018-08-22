
class Solution:
    def canJump(self, nums):
        # currMax当前最远能跳到什么<位置>
        currMax =nums[0]
        for i in range(len(nums)):
            if i >currMax:return False
            currMax = max(i+nums[i], currMax)
            if currMax>=len(nums)-1:return True
        return currMax>=len(nums)-1