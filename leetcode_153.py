# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '(%s, %s)' % (self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        result = []
        stopFlag = False
        for interval in intervals:
            if stopFlag:
                result.append(interval)
                continue

            if newInterval.end < interval.start:
                result.append(newInterval)
                result.append(interval)
                stopFlag = True
            elif newInterval.start > interval.end:
                result.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        if not stopFlag:
            result.append(newInterval)
        return result


s = Solution()
intervals = [Interval(1, 3), Interval(6, 9), Interval(10, 12)]
newInterval = Interval(2, 5)
for interval in s.insert(intervals, newInterval):
    print interval.__str__()
intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
newInterval = Interval(4, 9)
for interval in s.insert(intervals, newInterval):
    print interval.__str__()