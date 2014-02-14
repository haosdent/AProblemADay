public class Solution {
  public boolean searchMatrix(int[][] matrix, int target) {
    int m = matrix.length, n = matrix[0].length;
    int first = 0, last = m * n;
    for (; first < last;) {
      int mid = first + (last - first) / 2;
      int tmp = matrix[mid / n][mid % n];
      if (tmp < target) {
        first = mid + 1;
      } else if (tmp > target) {
        last = mid;
      } else {
        return true;
      }
    }
    return false;
  }
}


















