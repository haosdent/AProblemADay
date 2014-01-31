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
  public ArrayList<ArrayList<Integer>> pathSum(TreeNode root, int sum) {    
    ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
    ArrayList<Integer> cur = new ArrayList<Integer>();
    pathSum(root, sum, cur, result);
    return result;
  }
  public void pathSum(TreeNode root, int sum, ArrayList<Integer> cur, ArrayList<ArrayList<Integer>> result) {
    if (root == null) return;
    cur.add(root.val);
    if (root.left == null && root.right == null) {
      if (sum == root.val) {
        result.add(new ArrayList<Integer>(cur));
      }
    }
    pathSum(root.left, sum - root.val, cur, result);
    pathSum(root.right, sum - root.val, cur, result);
    cur.remove(cur.size() - 1);
  }
}
