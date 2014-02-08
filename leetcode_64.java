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
    for (ListNode cur = head; cur != null;) {
      ListNode pos = findInsertPos(dummy, cur.val);
      ListNode tmp = cur.next;
      cur.next = pos.next;
      pos.next = cur;
      cur = tmp;
    }
    return dummy.next;
  }

  public ListNode findInsertPos(ListNode head) {
    ListNode pre = null;
    for (ListNode cur = head; cur != null && cur.val <= x; pre = cur, cur = cur.next);
    return pre;
  }
}










