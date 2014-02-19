public class Solution {
  public ArrayList<ArrayList<Integer>> permute(int[] num) {
    Arrays.sort(num);
    ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
    do {
      ArrayList<Integer> tmp = new ArrayList<Integer>();
      for (int i = 0; i < num.length; i++) {
        tmp.add(num[i]);
      }
      result.add(tmp);
    } while (nextPermute(num));

    return result;
  }

  public boolean nextPermute(int[] num) {
    int i, j;
    for (i = num.length - 2; (i >= 0) && (num[i] >= num[i + 1]); i--);
    if (i < 0) {
      return false;
    }

    for (j = num.length - 1; num[i] >= num[j]; j--);
    int tmp = num[i];
    num[i] = num[j];
    num[j] = tmp;
    for (i = i + 1, j = num.length - 1; i < j; i++, j--) {
      tmp = num[i];
      num[i] = num[j];
      num[j] = tmp;
    }
    return true;
  }
}
