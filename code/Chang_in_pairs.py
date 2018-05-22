
# 链表成对调换
# 1->2->3->4 转换为 2->1->4->3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swaPairs(self, head):
        if head != None and head.next != None:
            tmp = head.next
            head.next = self.swaPairs(tmp.next)  # 使1指向4
            tmp.next = head # 使 2 指向 1， 下一轮 4 指向 3
            return tmp
        return head