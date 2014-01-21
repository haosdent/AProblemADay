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
  public TreeNode sortedArrayToBST(int[] num) {
    return sortedArrayToBST(num, 0, num.length);
  }
  public TreeNode sortedArrayToBST(int[] num, int start, int end) {
    if (end - start <= 0) return null;
    int mid = (end - start) / 2 + start;
    TreeNode node = new TreeNode(num[mid]);
    node.left = sortedArrayToBST(num, start, mid);
    node.right = sortedArrayToBST(num, mid + 1, end);
    return node;
  }
}
