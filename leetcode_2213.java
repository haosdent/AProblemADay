public class Solution {
  public void reorderList(ListNode head) {
    if (head == null) {
      return;
    }

    ListNode slow = head;
    ListNode fast = head.next;
    while (fast != null) {
      if (fast.next == null) {
        break;
      }
      fast = fast.next.next;
      slow = slow.next;
    }

    ListNode first = head;
    ListNode second = slow.next;
    slow.next = null;
    second = reverse(second);

    while (first != null && second != null) {
      ListNode preFirst = first;
      ListNode preSecond = second;
      first = first.next;
      second = second.next;
      preFirst.next = preSecond;
      preSecond.next = first;
    }
  }

  public ListNode reverse(ListNode node) {
    ListNode cur = node;
    ListNode prePre = null;
    ListNode pre = cur;
    while (cur != null) {
      pre = cur;
      cur = cur.next;
      pre.next = prePre;
      prePre = pre;
    }
    return pre;
  }
}
