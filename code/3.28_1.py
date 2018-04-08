# -*- coding: utf-8 -*-


# 给定一个二叉树和其中的一个结点，请找出中序遍历(左根右)顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


class Solution:
    # 根始终是左的下一个节点，出发点在左节点
    def GetNext(self, pNode):
        if not pNode:
            return pNode
        # 向下
        if pNode.right:
            left1 = pNode.right
            while left1.left1:
                left1 = left1.left
            return left1
        # 向上
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
            pNode = tmp
