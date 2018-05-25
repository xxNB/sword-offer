#########################################################
# 链表求和 ||
#########################################################

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "%s-->%s" % (self.val, self.next)


class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """

    def addLists2(self, l1, l2):

        s1 = self.getSize(l1)
        s2 = self.getSize(l2)
        s = max(s1, s2)

        p = h = ListNode(0)
        while s:
            p.next = ListNode(0)
            p = p.next
            if s <= s1:
                p.val += l1.val
                l1 = l1.next
            if s <= s2:
                p.val += l2.val
                l2 = l2.next
            s -= 1
        p = h
        while p:
            q = p.next
            while q and q.val == 9:
                q = q.next
            if q and q.val > 9:
                while p != q:
                    p.val += 1
                    p = p.next
                    p.val -= 10
            else:
                p = q
        return h if h.val else h.next

    def getSize(self, h):
        c = 0
        while h:
            c += 1
            h = h.next
        return c


l1 = ListNode(6)
l1.next = ListNode(1)
l1.next.next = ListNode(7)
# l1.next.next.next = ListNode(None)
l2 = ListNode(3)
l2.next = ListNode(9)
l2.next.next = ListNode(5)
# l2.next.next.next = ListNode(None)
print(l1)
print(l2)

c = Solution()
c.addLists2(l1, l2)