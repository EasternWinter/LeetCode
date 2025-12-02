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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode temp = new ListNode();
        ListNode ans = temp;
        while(list1 != null && list2 != null) {
            if(list1.val <= list2.val) {
                ans.next = list1;
                list1 = list1.next;
            }
            else {
                ans.next = list2;
                list2 = list2.next;
            }
            ans = ans.next;
        }
        if(list2 != null) {
            ans.next = list2;
        }
        else if(list1 != null) {
            ans.next = list1;
        }
        return temp.next;
    }
    
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        return divideAndConquer(lists, 0, lists.length - 1);
    }

    private ListNode divideAndConquer(ListNode[] lists, int left, int right) {
        if (left == right) return lists[left];

        int mid = left + (right - left) / 2;
        ListNode l1 = divideAndConquer(lists, left, mid);
        ListNode l2 = divideAndConquer(lists, mid + 1, right);
        return mergeTwoLists(l1, l2);
    }
}