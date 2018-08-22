# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    first, second = 65535, 65535
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.secondmin(root, first=self.first, second=self.second)
        if self.second!=65535:
            return self.second
        return -1

    def secondmin(self,root,first,second):
        if not root:
            return
        else:
            if root.val<first:
                second = first
                self.first = root.val
            elif first<root.val and root.val<second:
                self.second = root.val
            self.secondmin(root.left, self.first, self.second)
            self.secondmin(root.right, self.first, self.second)
