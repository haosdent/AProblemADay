/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
  public TreeNode sortedListToBST(ListNode head) {
    int len = 0;
    ListNode p = head;
    while (p != null) {
      len++;
      p = p.next;
    }
    return sortedListToBST(head, len);
  }
  public TreeNode sortedListToBST(ListNode head, int dist) {
    if (dist <= 0) return null;

    int mid = dist / 2;
    TreeNode left = sortedListToBST(head, mid);
    for (int i = 1; i <= mid; i++) head = head.next;
    TreeNode node = new TreeNode(head.val);
    node.left = left;
    head = head.next;
    TreeNode right = sortedListToBST(head, dist - mid - 1);
    node.right = right;

    return node;
  }
}
