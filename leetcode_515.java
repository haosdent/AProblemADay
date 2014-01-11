public class Solution {
    public ArrayList<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
      Stack<ArrayList<Integer>> resultStack = new Stack<ArrayList<Integer>>();
      ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
      List<TreeNode> pre = new LinkedList<TreeNode>();
      List<TreeNode> cur = new LinkedList<TreeNode>();
      if (root != null) cur.add(root);

      while (cur.size() != 0) {
        ArrayList<Integer> tmp = new ArrayList<Integer>();
        for (TreeNode node : cur) {
          tmp.add(node.val);
          if (node.left != null) pre.add(node.left);
          if (node.right != null) pre.add(node.right);
        }
        resultStack.push(tmp);
        cur = pre;
        pre = new LinkedList<TreeNode>();
      }

      while (resultStack.size() != 0) {
        result.add(resultStack.pop());
      }

      return result;
    }
}














