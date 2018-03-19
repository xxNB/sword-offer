# -*- coding: utf-8 -*-

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        l = []
        while head != None:
            l.append(head)
            head = head.next
        if k > len(l) or k < 1:
            return
        return l[-k]
