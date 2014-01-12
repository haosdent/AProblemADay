public class Solution {
  public boolean isBalanced(TreeNode root) {
    return getHeight(root) >= 0;
  }

  public int getHeight(TreeNode root) {
    if (root == null) return 0;

    int left = getHeight(root.left);
    int right = getHeight(root.right);
    if (left < 0 || right < 0 || Math.abs(left - right) > 1) return -1;

    return Math.max(left, right) + 1;
  }
}










