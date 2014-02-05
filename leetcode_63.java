/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
  public ListNode mergeKLists(ArrayList<ListNode> lists) {
    ListNode pre = new ListNode(-1);
    ListNode head = pre;
    pre.next = lists.first();
    ArrayList<ListNode> tmpLists = lists;
    boolean flag = true;
    while (flag) {
      lists = tmpLists;
      if (tmpLists.size() == 0) {
        flag = false
      }
      for (ListNode list : lists) {
        if 
      }
    }
  }

  public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode pre = new ListNode(-1);
    ListNode head = pre;
    pre.next = l1;
    while (l1 != null && l2 != null) {
      if (l1.val > l2.val) {
        pre.next = l2;
        pre = pre.next;
        l2 = l2.next;
        pre.next = l1;
      } else {
        pre = pre.next;
        l1 = l1.next;
      }
    }
    if (l2 != null) {
      pre.next = l2;
    }
    return head.next;
  }
}
