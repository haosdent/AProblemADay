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
  public TreeNode buildTree(int[] preorder, int[] inorder) {
    return buildTree(preorder, 0, preorder.length, inorder, 0, inorder.length);
  }

  public TreeNode buildTree(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd) {
    if (preStart == preEnd) return null;
    if (inStart == inEnd) return null;

    TreeNode root = new TreeNode(preorder[preStart]);
    int pos = inStart;
    for (int i = inStart; i < inEnd; i++) {
      if (inorder[i] == preorder[preStart]) {
        pos = i;
        break;
      }
    }
    root.left = buildTree(preorder, preStart + 1, pos - inStart + preStart + 1, inorder, inStart, pos);
    root.right = buildTree(preorder, pos - inStart + preStart + 1, preEnd, inorder, pos + 1, inEnd);

    return root;
  }
}


















