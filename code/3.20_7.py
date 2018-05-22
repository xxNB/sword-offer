# -*- coding: utf-8 -*-

# 操作给定的二叉树，将其变换为源二叉树的镜像。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Mirror(self, root):
        if root is None:
            return
        # 左为右，右为左
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)


