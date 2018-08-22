package leetcode;

/**
 * Created by zhangxin on 2018/8/9.
 */
public class rotateList {



    public ListNode rotateRight(ListNode head, int k){
       if (head==null||head.next==null) return head;
        ListNode index = head;
        int len =1;
        while (index.next!=null){
            index = index.next;
            len++;
        }
        index.next = head;
        // len - k%len
        for(int i =1;i<len-k%len;i++){
            head = head.next;
        }
        ListNode res = head.next;
        head.next = null;
        return res;
    }
}
