public class Solution {
  public int searchInsert(int[] A, int target) {
    int first = 0, last = A.length;
    int mid = (last - first) / 2;
    while (first < last) {
      mid = first + (last - first) / 2;
      if (target > A[mid]) {
        first = mid + 1;
      } else if (target < A[mid]) {
        last = mid;
      } else if (target == A[mid]) {
        return mid;
      }
    }
    return first + 1;
  }
}
