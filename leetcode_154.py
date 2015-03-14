# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '(%s, %s)' % (self.start, self.end)

class Solution:
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

    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        result = []
        for interval in intervals:
            result = self.insert(result, interval)
        return result

s = Solution()
intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
for interval in s.merge(intervals):
    print interval.__str__()