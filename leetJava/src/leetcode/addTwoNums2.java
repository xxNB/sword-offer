package leetcode;

import java.util.Stack;

/**
 * Created by zhangxin on 2018/8/9.
 */


public class addTwoNums2 {


    public ListNode addTwoNum(ListNode l1, ListNode l2) {
        if (l1 == null)
            return l2;
        if (l2 == null)
            return l1;
        Stack<Integer> s1 = new Stack<>();
        Stack<Integer> s2 = new Stack<>();
        while (l1 != null) {
            s1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            s2.push(l2.val);
            l2 = l2.next;
        }
        int sum = 0;
        ListNode dummy = new ListNode(0);
//        ListNode cur = dummy;
        while (!s1.isEmpty() || !s2.isEmpty()) {
            if (!s1.isEmpty())
                sum += s1.pop();
            if (!s2.isEmpty())
                sum += s2.pop();
            ListNode head = new ListNode(sum / 10);
            dummy.val = sum % 10;
            head.next = dummy;
            dummy = head;
            sum /= 10;
        }
        if (dummy.val == 0)
            dummy = dummy.next;
        return dummy;
    }

}
