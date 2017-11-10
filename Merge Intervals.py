# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intersec = 0
        s, e = newInterval.start, newInterval.end
        idx = 0
        intervals.sort(key = lambda x: x.start)
        for idx, i in enumerate(intervals):
            if i.start > newInterval.end:
                break
            if newInterval.start > i.end:
                continue
            else:
                s = min(newInterval.start, i.start)
                e = max(newInterval.end, i.end)
                intersec += 1
        if intersec > 0:
            intervals[idx - intersec:idx] = []
        intervals.insert(idx-intersec, Interval(s, e))
        return intervals

sol = Solution()
a = []
a = sol.insert(a,Interval(1,3))
a = sol.insert(a,Interval(6,9))
a = sol.insert(a,Interval(1,5))
print a




