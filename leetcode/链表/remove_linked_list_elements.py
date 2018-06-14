#########################################################
# 删除链表中带元素
#########################################################

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):

        # 设置虚拟节点方便删除第一个
        new_head = pre = ListNode(0)
        pre.next = head
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                # pre往下走
                pre = pre.next
            # head往下走
            head = head.next
        return new_head.next