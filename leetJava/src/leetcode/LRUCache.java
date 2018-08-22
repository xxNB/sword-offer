package leetcode;


import java.util.HashMap;

/**
 * Created by zhangxin on 2018/8/9.
 */
public class LRUCache {

    /**
     * Your LRUCache object will be instantiated and called as such:
     * LRUCache obj = new LRUCache(capacity);
     * int param_1 = obj.get(key);
     * obj.put(key,value);

     hashMap + Double linked list
     */
    class Node{
        int key;
        int value;
        Node next;
        Node pre;
        public Node(int key, int value){
            this.key = key;
            this.value = value;
        }
    }

    private HashMap<Integer, Node> map;
    private int capacity;
    private Node head;
    private Node tail;

    public LRUCache(int capacity) {
        map = new HashMap<>();
        this.capacity = capacity;
        head = null;
        tail = null;

    }

    public int get(int key) {
        Node curNode = map.remove(key);
        if (curNode.next == null)
            tail = curNode.pre;
        else if(curNode.pre ==null)
            head = curNode.next;
        else {curNode.pre.next = curNode.next.next;}
        capacity--;
        return curNode.value;

    }

    public void put(int key, int value) {
        Node node = map.get(key);
        if (node!=null){
            Node newNode = new Node(key, value);
            tail.next = newNode;
            tail = newNode;
            map.put(key, newNode);
            capacity--;
        }else {
            Node newNode = new Node(key, value);
            if (capacity ==0){
                Node temp = head;
                head = head.next;
                map.remove(temp.key);
                capacity++;
            }
            if (head==null&&tail==null){
                head = newNode;
            }else {
                tail.next = newNode;
            }
            tail = newNode;
            map.put(key, newNode);
            capacity--;
        }
    }
    public static void main(String args[]){
        LRUCache cache = new LRUCache(2);
        cache.put(1,1);
        cache.put(2,2);
        System.out.println(cache.get(1));
    }
}
