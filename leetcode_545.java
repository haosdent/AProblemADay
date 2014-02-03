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
  public int max = Integer.MIN_VALUE;
  public int maxPathSum(TreeNode root) {
    dfs(root);
    return max;
  }
  public int dfs(TreeNode root) {
    if (root == null) return 0;
    int l = dfs(root.left);
    int r = dfs(root.right);
    int s = root.val;
    if (l > 0) s += l;
    if (r > 0) s += r;
    if (s > max) max = s;
    return Math.max(r, l) > 0? Math.max(r, l) + root.val : root.val;
  }
} 


















