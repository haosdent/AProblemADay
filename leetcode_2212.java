public class Solution {
  public ListNode detectCycle(ListNode head) {
    if (head == null) {
      return null;
    }

    ListNode slow = head;
    ListNode fast = head.next;
    while (fast != null) {
      slow = slow.next;
      fast = fast.next;
      if (fast != null) {
        fast = fast.next;
      }
      if (slow == fast) {
        break;
      }
    }

    if (fast == null) {
      return null;
    }

    ListNode find = null;
    while (slow != null) {
      if (find == null) {
        find = head;
      } else {
        find = find.next;
      }
      slow = slow.next;
      if (slow == find) {
        break;
      }
    }

    return slow;
  }
}
