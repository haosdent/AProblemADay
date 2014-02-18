public class Solution {
  public ArrayList<ArrayList<Integer>> permute(int[] num) {
    Arrays.sort(num);
    ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
    do {
      ArrayList<Integer> tmp = new ArrayList<Integer>();
      for (int i; i < num.length; i++) {
        tmp.add(num[i]);
      }
      result.add(tmp);
    } while (nextPremute(num));

    return result;
  }

  public boolean nextPremute(int[] num) {
    
  }
}















