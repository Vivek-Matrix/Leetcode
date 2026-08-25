/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {

        if(head == null || head.next == null) {return head;}
        ListNode even = head.next;
        ListNode etemp = even;
        ListNode otemp = head;
        while(etemp!=null && etemp.next!=null){
            otemp.next = etemp.next;
            otemp = otemp.next;
            etemp.next = otemp.next;
            etemp = otemp.next;
        }
        otemp.next = even;
        return head;

    }
}