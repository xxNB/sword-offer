# -*- coding: utf-8 -*-

# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（
# 注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

class RandomListNode:
    def __init__(self, x):
        self.label = x # 节点值
        self.next = None # 指向下一个节点
        self.random = None # 指向任意一个节点


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        p = RandomListNode(pHead.label)
        p.next = pHead.next
        p.random = pHead.random

        p.next = self.Clone(pHead.next)
        # 返回复杂链表的head
        return p
