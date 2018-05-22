class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addtwonumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        tmp = ListNode(0) 
        res = tmp
        flag = 0
        while l1 or l2:
            tmpsum = 0
            if l1:
                tmpsum += l2.val
                l2 = l2.next
            tmpres = ((tmpsum+flag) % 10)  # 取余
            flag = ((tmpsum + flag) // 10)  # 取商
            res.next = ListNode(tmpres)
            res = res.next
        if flag:
            res.next = ListNode(1)
        res = tmp.next
        del tmp
        return res

import random