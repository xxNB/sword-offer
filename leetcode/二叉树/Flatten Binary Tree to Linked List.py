"""
453. Flatten Binary Tree to Linked List
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

Example
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
Challenge
Do it in-place without any extra memory.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):

        """
        非递归的先序遍历
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pointer = dummy = TreeNode(None)
        stack = [root]
        while stack:
            top = stack.pop()
            if not top:
                continue
            stack.append(top.right)
            stack.append(top.left)
            pointer.right = top
            pointer.left = None
            pointer = top
