#########################################################
# 链表求和 ||
#########################################################
"""
221. Add Two Numbers II
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in forward order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

Example
Given 6->1->7 + 2->9->5. That is, 617 + 295.

Return 9->1->2. That is, 912.
"""
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
        print("h", h)
        p = h
        print("p", p)
        while p:
            # 使用双指针解决，q始终在p后面
            q = p.next
            print("q", q)
            while q and q.val == 9:
                # 有几个9，就比p往后推几个
                q = q.next
            if q and q.val > 9:
                while p != q:
                    # 恢复到q的位置
                    p.val += 1
                    p = p.next
                    p.val -= 10
            else:
                # 直接把p按到q到位置
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
print(c.addLists2(l1, l2))