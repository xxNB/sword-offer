"""
67. Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [1,3,2].

Challenge
Can you do it without recursion?
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    中序遍历
    1 . 添加所有最左边节点到栈。
    2. pop stack 然后添加到结果。
    3 .查找当前node的右边节点是否为空， 如果不为空，重复step 1。
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []

        result = []
        stack = []

        while root:
            stack.append(root)
            root = root.left

        while stack:
            curNode = stack.pop()
            result.append(curNode.val)

            if curNode.right:
                curNode = curNode.right
                while curNode:
                    stack.append(curNode)
                    curNode = curNode.left

        return result
