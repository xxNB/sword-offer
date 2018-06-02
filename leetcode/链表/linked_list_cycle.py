#########################################################
# 判断是否带环链表
#########################################################


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        # write your code here
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
