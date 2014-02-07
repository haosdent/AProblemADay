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
  public ListNode insertionSortList(ListNode head) {
    ListNode dummy = new ListNode(Integer.MIN_VALUE);
    dummy.next = head;
    for (ListNode cur = head, pre = dummy; cur != null;) {
      ListNode tmp = cur.next;
      pre.next = cur.next;
      cur.next = null;
      ListNode pos = findInsertPos(dummy, pre, cur.val);
      cur.next = pos.next;
      pos.next = cur;
      cur = tmp;
    }
    return dummy.next;
  }

  public ListNode findInsertPos(ListNode head, ListNode stop, int x) {
    ListNode pre = head;
    for (ListNode cur = head; cur != stop && cur.val <= stop.val; pre = cur, cur = cur.next);
    return pre;
  }
}
