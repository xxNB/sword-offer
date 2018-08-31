class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mx = 0
        mx_idx = 0
        for i in range(len(nums)):
            if mx<nums[i]:
                mx = nums[i]
                mx_idx=i

        node = TreeNode(mx)
        leftArr = nums[0:mx_idx]
        rightArr = nums[mx_idx+1,-1]
        node.left =self.constructMaximumBinaryTree(leftArr)
        node.right = self.constructMaximumBinaryTree(rightArr)
        return node

