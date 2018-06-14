
#########################################################
# 反转链表 ||
#########################################################


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}->{}->{}".format(self.val, self.next.val, self.next.next.val)


class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """

    def reverseBetween(self, head, m, n):
        # write your code here
        # 设置虚拟节点

        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        front, prev, last = None, None, None
        if m == 1:
            prev = cur
            last = cur.next
        for i in range(m - 1):
            #
            cur = cur.next
            prev = cur
            last = cur.next

        for i in range(m, n + 1):
            # print("before reserved", dummy.next)
            # new_head>prev>cur>null
            cur = prev.next
            prev.next = cur.next
            cur.next = front
            front = cur

            # print("after reserved", dummy.next)
        cur = prev.next
        prev.next = front
        last.next = cur
        return dummy.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(7)
l1.next.next.next.next.next.next = ListNode(9)

r = Solution()
print(r.reverseBetween(l1, 3, 6))