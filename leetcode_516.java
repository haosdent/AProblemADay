public class Solution {
    public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode root) {
      ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
      List<TreeNode> pre = new LinkedList<TreeNode>();
      List<TreeNode> cur = new LinkedList<TreeNode>();
      if (root != null) cur.add(root);
      boolean isReverse = false;

      while (cur.size() != 0) {
        ArrayList<Integer> tmp = new ArrayList<Integer>();
        for (TreeNode node : cur) {
          tmp.add(node.val);
          if (node.left != null) pre.add(node.left);
          if (node.right != null) pre.add(node.right);
        }
        if (isReverse) Collections.reverse(tmp);
        result.add(tmp);
        cur = pre;
        pre = new LinkedList<TreeNode>();
        isReverse = !isReverse;
      }

      return result;
    }
}















