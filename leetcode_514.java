public class Solution {
    public ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) {
      if (root == null) {
        return new ArrayList<ArrayList<Integer>>();
      }

      ArrayList<ArrayList<Integer>> leftResult = levelOrder(root.left);
      ArrayList<ArrayList<Integer>> rightResult = levelOrder(root.right);
      ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
      ArrayList<Integer> cur = new ArrayList<Integer>();
      cur.add(root.val);
      result.add(cur);
      int leftSize = leftResult.size();
      int rightSize = rightResult.size();
      int size = leftSize > rightSize? leftSize : rightSize;
      for (int i = 0; i < size; i++) {
        ArrayList<Integer> tmp = new ArrayList<Integer>();
        if (i < leftSize) {
          tmp.addAll(leftResult.get(i));
        }
        if (i < rightSize) {
          tmp.addAll(rightResult.get(i));
        }
        result.add(tmp);
      }
      return result;
    }
}


















