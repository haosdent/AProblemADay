public class Solution {
  public ArrayList<ArrayList<Integer>> subsets(int[] S) {
    ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
    result.add(new ArrayList<Integer>());
    Arrays.sort(S);
    for (int i = 0; i < S.length; i++) {
      int l = result.size();
      for (int j = 0; j < l; j++) {
        ArrayList<Integer> set = result.get(j);
        ArrayList<Integer> newSet = new ArrayList<Integer>(set);
        newSet.add(S[i]);
        result.add(newSet);
      }
    }
    return result;
  }
}
