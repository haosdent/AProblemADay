/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; left = null; right = null; }
 * }
 */
public class Solution {
  public ArrayList<TreeNode> generateTrees(int n) {
    if (n == 0) return generateTrees(1, 0);
    return generateTrees(1, n);
  }
  public ArrayList<TreeNode> generateTrees(int start, int end) {
    ArrayList<TreeNode> subs = new ArrayList<TreeNode>();

    if (start > end) {
      subs.add(null);
      return subs;
    }

    for (int i = start; i <= end; i++) {
      ArrayList<TreeNode> leftSubs = generateTrees(start, i - 1);
      ArrayList<TreeNode> rightSubs = generateTrees(i + 1, end);
      for (TreeNode left : leftSubs) {
        for (TreeNode right : rightSubs) {
          TreeNode node = new TreeNode(i);
          node.left = left;
          node.right = right;
          subs.add(node);
        }
      }
    }

    return subs;
  }
}
