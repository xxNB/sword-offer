#########################################################
# 俩个链表带交叉
#########################################################
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        # write your code here
        if not headA or not headB:
            return None
        p, q = headA, headB
        while p and q and p != q:
            p = p.next
            q = q.next
            if p == q:
                return p
            if not q:
                q = headA
            if not p:
                p = headB
        return p
