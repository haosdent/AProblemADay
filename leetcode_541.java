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
  public int minDepth(TreeNode root) {
    return minDepth(root, false);
  }

  public int minDepth(TreeNode root, boolean hasBrother) {
    if (root == null) {
      if (hasBrother) {
        return Integer.MAX_VALUE;
      } else {
        return 0;
      }
    }

    return 1 + Math.min(minDepth(root.left, root.right != null), minDepth(root.right, root.left != null));
  }
}


















