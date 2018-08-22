package leetcode;

/**
 * Created by zhangxin on 2018/8/9.
 */
public class removeNthFromEnd {

    public ListNode removeNthFromEnd(ListNode head, int n){
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode fast = dummy;
        ListNode slow = dummy;
        for(int i=0; i<n+1; i++){
            fast = fast.next;
        }
        while (fast!=null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }
    public static void main(String strs[]){
        System.out.println("ss");
    }
}
