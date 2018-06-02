
#########################################################
# 反转链表 ||
#########################################################


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "%s-->%s" % (self.val, self.next)


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
        prev = dummy
        for i in range(m - 1):
            # pre截止为   要反转的前俩个
            print("prev", prev)
            prev = prev.next
        new_head = prev
        prev = new_head.next
        # 定位到要反转的那个节点 !
        cur = prev.next
        # print("prev", prev)
        # print("cur", cur)
        # print("new_head", new_head)
        for i in range(m, n):
            # print("before reserved", dummy.next)
            prev.next = cur.next
            cur.next = new_head.next
            new_head.next = cur
            cur = cur.next
            # print("after reserved", dummy.next)

        return dummy.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(7)
l1.next.next.next.next.next.next = ListNode(9)

print("l1", l1)
r = Solution()
print(r.reverseBetween(l1, 4, 6))