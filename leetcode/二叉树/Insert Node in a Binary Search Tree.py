"""
85. Insert Node in a Binary Search Tree
Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

Example
Given binary search tree as follow, after Insert node 6, the tree should be:

  2             2
 / \           / \
1   4   -->   1   4
   /             / \
  3             3   6
Challenge
Can you do it without recursion?
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    # def insertNode(self, root, node):
    # write your code here
    class Solution:
        """
        在二叉树里插入一个node
        @param: root: The root of the binary search tree.
        @param: node: insert this node into the binary search tree
        @return: The root of the new binary search tree.
        """

        # def insertNode(self, root, node):
        # write your code here
        def insertNode(self, root, node):
            if root is None:
                return node
            if root.val > node.val:
                root.left = self.insertNode(root.left, node)
            else:
                root.right = self.insertNode(root.right, node)
            return root
