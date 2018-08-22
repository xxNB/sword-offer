# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        分治算法
        """
        if nums is None or len(nums) == 0:
            return None
        return self.creat(nums, 0, len(nums) - 1)

    def creat(self, nums, l, r):
        if l > r:
            return None
        mid = (l + r + 1) / 2
        root = TreeNode(nums[mid])
        root.left = self.creat(nums, l, mid - 1)
        root.right = self.creat(nums, mid + 1, r)
        return root
