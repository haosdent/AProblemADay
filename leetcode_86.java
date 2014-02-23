public class Solution {
  final String[] keys = {" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
  public ArrayList<String> letterCombinations(String digits) {
    ArrayList<String> result = new ArrayList<String>();
    dfs(digits, 0, "", result);
    return result;
  }
  public void dfs(String digits, int cur, String path, ArrayList<String> result) {
    if (cur == digits.length()) {
      result.add(path);
      return;
    }
    for (char k : keys[digits.charAt(cur) - '0'].toCharArray()) {
      dfs(digits, cur + 1, path + k, result);
    }
  }
}


















