public class Solution {
  public ArrayList<ArrayList<Integer>> subsetsWithDup(int[] num) {
    ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
    result.add(new ArrayList<Integer>());
    Arrays.sort(num);
    int preLen = 0;
    for (int i = 0; i < num.length; i++) {
      int l = result.size();
      for (int j = 0; j < l; j++) {
        if (i == 0 || num[i] != num[i - 1] || j >= preLen) {
          ArrayList<Integer> set = result.get(j);
          ArrayList<Integer> newSet = new ArrayList<Integer>(set);
          newSet.add(num[i]);
          result.add(newSet);
        }
      }
      preLen = l;
    }
    return result;
  }
}

















