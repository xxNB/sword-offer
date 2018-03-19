# -*- coding: utf-8 -*-

# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        # 根节点在中序遍历里的位置
        pos = tin.index(pre[0])
        # 拿出最上层的左部分和右部分再次迭代
        root.left = self.reConstructBinaryTree(pre[1:1 + pos], tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos + 1:], tin[pos + 1:])
        return root
