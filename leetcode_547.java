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
  public int sumNumbers(TreeNode root) {
    return dfs(root, 0);
  }
  public int dfs(TreeNode root, int pre) {
    if (root == null) return 0;
    pre = pre * 10 + root.val;
    if (root.left == null && root.right == null) {
      return pre;
    }
    return dfs(root.left, pre) + dfs(root.right, pre);
  }
}
