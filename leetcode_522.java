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
  public TreeNode buildTree(int[] inorder, int[] postorder) {
    return buildTree(inorder, 0, inorder.length, postorder, 0, postorder.length);
  }

  public TreeNode buildTree(int[] inorder, int inStart, int inEnd, int[] postorder, int postStart, int postEnd) {
    if (postStart == postEnd) return null;
    if (inStart == inEnd) return null;

    TreeNode root = new TreeNode(postorder[postEnd - 1]);
    int pos = inStart;
    for (int i = inStart; i < inEnd; i++) {
      if (inorder[i] == root.val) {
        pos = i;
        break;
      }
    }
    root.left = buildTree(inorder, inStart, pos, postorder, postStart, postStart + pos - inStart);
    root.right = buildTree(inorder, pos + 1, inEnd, postorder, postStart + pos - inStart, postEnd - 1);

    return root;
  }
}


















