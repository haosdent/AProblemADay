public class Solution {
  public int[] searchRange(int[] A, int target) {
    int first = 0, last = A.length;
    int start = -1, end = -1;
    for (; first < last;) {
      int mid = first + (last - first) / 2;
      if (A[mid] < target) {
        first = mid + 1;
      } else if (A[mid] > target) {
        last = mid;
      } else {
        start = first;
        end = last - 1;
        break;
      }
    }

    for (int i = start, j = end; i < j; i++, j--) {
      if (A[start] < target) {
        start++;
      }
      if (A[end] > target) {
        end--;
      }
    }

    return new int[]{start, end};
  }
}
