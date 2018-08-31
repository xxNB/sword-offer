# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        使用递归的思想，首先使用DFS思路找到左子树的最左节点，然后将该最左节点的父节点和右子树断开，把该最左节点连接到父节点的右节点上，
        左节点置为null，再把原右子树连接到原左子树的最右节点上，再往上遍历
        """
        # if not root:
        #     return None
        # if root.left:
        #     self.flatten(root.left)
        # if root.right:
        #     self.flatten(root.right)
        #
        # tmp = root.right
        # root.right = root.left
        # root.left = None
        # while root.right:
        #     root = root.right
        # root.right = tmp
        #
        cur=root
        while cur:
            if cur.left:
                p = cur.left
                while p.right:
                    p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

