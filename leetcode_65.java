/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
  public ListNode sortList(ListNode head) {
    if (head == null || head.next == null) return head;

    ListNode slow = head, fast = head;
    for (; fast.next != null && fast.next.next != null;) {
      slow = slow.next;
      fast = fast.next.next;
    }

    ListNode first = sortList(slow.next);
    slow.next = null;
    ListNode second = sortList(head);
    return mergeTwoList(first, second);
  }

  public ListNode mergeTwoList(ListNode first, ListNode second) {
    ListNode pre = new ListNode(-1);
    ListNode head = pre;
    pre.next = first;
    for (; first != null && second != null; ) {
      if (first.val > second.val) {
        pre.next = second;
        second = second.next;
        pre = pre.next;
        pre.next = first;
      } else {
        pre = pre.next;
        first = first.next;
      }
    }
    if (second != null) {
      pre.next = second;
    }
    return head.next;
  }
}
