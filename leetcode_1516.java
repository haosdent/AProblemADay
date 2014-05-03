/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
public class Solution {
  public int maxPoints(Point[] points) {
    int max = 0;
    for (int i = 0; i < points.length; i++) {
      int tmpMax = 0;
      int base = 1;
      Map<Double, Integer> slopeMap = new HashMap<Double, Integer>();
      Point curPoint = points[i];
      for (int l = 0; l < points.length; l++) {
        Point tmpPoint = points[l];
        if (tmpPoint.equals(curPoint)) {
          continue;
        }
        if (tmpPoint.x == curPoint.x && tmpPoint.y == curPoint.y) {
          base++;
          continue;
        }

        double slope = (tmpPoint.x - curPoint.x + 0.0) / (tmpPoint.y - curPoint.y + 0.0);
        Integer count = slopeMap.get(slope);
        if (count == null) {
          count = 1;
        } else {
          count++;
        }
        if (count > tmpMax) {
          tmpMax = count;
        }
        slopeMap.put(slope, count);
      }
      tmpMax += base;
      if (max < tmpMax) {
        max = tmpMax;
      }
    }

    return max;
  }
}