# -*- coding: utf-8 -*-

# 输入一颗二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向

class Solution:
    def convert(self, prootoftree):
        if not prootoftree:
            return prootoftree
        if not prootoftree.left and not prootoftree.right:
            return prootoftree

        # 处理左子树
        self.convert(prootoftree.left)
        left = prootoftree.left

        # 连接根与左子树的最大结点
        if left:
            while left.right:
                left = left.right
            prootoftree.left, left.right = left, prootoftree

        # 处理右子树
        self.convert(prootoftree.right)
        right = prootoftree.right

        # 连接根与右子树最小结点
        if right:
            while right.left:
                right = right.left
            prootoftree.right, right.left = right, prootoftree

        while prootoftree.left:
            prootoftree = prootoftree.left
        return prootoftree
