package leetcode;

/**
 * Created by zhangxin on 2018/8/9.
 */
public class swapNodeInPairs {

    public ListNode swapPairs(ListNode head){
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode current = dummy;
        while (current.next !=null&&current.next.next!=null){
            swap2(current);
            current = current.next.next;
        }
        return dummy.next;
    }
    private void swap2(ListNode pre){
        ListNode dummy = pre.next;
        pre.next = dummy.next;
        dummy.next = dummy.next.next;
        pre.next.next = dummy;
    }
}
