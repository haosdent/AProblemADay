public class Solution {
  public void sortColors(int[] A) {
    int red = 0, blue = A.length - 1;
    for (int i = 0; i < blue + 1;) {
      if (A[i] == 0) {
        int tmp = A[red];
        A[red] = A[i];
        A[i] = tmp;
        i++;
        red++;
      } else if (A[i] == 2) {
        int tmp = A[blue];
        A[blue] = A[i];
        A[i] = tmp;
        blue--;
      } else {
        i++;
      }
    }
  }
}
