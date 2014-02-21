public class Solution {
  public ArrayList<ArrayList<Integer>> combine(int n, int k) {
    ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
    Stack<Integer> path = new Stack<Integer>();
    dfs(n, k, 1, 0, path, result);
    return result;
  }
  public void dfs(int n, int k, int start, int cur, Stack<Integer> path, ArrayList<ArrayList<Integer>> result) {
    if (cur == k) {
      ArrayList<Integer> tmp = new ArrayList<Integer>(path);
      result.add(tmp);
      return;
    }
    for (int i = start; i <= n; i++) {
      path.push(i);
      dfs(n, k, i + 1, cur + 1, path, result);
      path.pop();
    }
  }
}
