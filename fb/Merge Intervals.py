# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key = lambda i:(i.start, i.end))
        res = [intervals[0]]
        for inter in intervals[1:]:
            if inter.start <= res[-1].end:
                res[-1].end = max(inter.end, res[-1].end)
            else:
                res.append(inter)
        return res

sol =Solution()
intervals = []
# intervals.append(Interval(1,3))
# intervals.append(Interval(2,6))
# intervals.append(Interval(8,10))
# intervals.append(Interval(15,18))

intervals.append(Interval(1,6))
intervals.append(Interval(8,10))
intervals.append(Interval(15,18))
res = sol.merge([])
print res

