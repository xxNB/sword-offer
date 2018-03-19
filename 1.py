# -*- coding: utf-8 -*-

# 输入一个链表，从尾部到头打印链表每个节点的值

class Solution:
    def printListFromTailToHead(self, listNode):
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l
