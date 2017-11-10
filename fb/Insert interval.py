
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i, s_p, e_p = 0,0,0
        tmp = Interval(newInterval.start, newInterval.end)
        if len(intervals) == 0:
            return [newInterval]
        while i < len(intervals) and intervals[i].start < newInterval.start and intervals[i].end < newInterval.start:
            i+=1
        if i < len(intervals) and intervals[i].start > newInterval.start:
            tmp.start = newInterval.start
        else:
            if i < len(intervals):
                tmp.start = intervals[i].start
        s_p = i
        while i < len(intervals) and intervals[i].start < newInterval.end and intervals[i].end < newInterval.end:
            i+=1
        if i < len(intervals) and intervals[i].start > newInterval.end:
            tmp.end = newInterval.end
            i-=1
        else:
            if i < len(intervals):
                tmp.end = intervals[i].end
        e_p = i
        res = intervals[:s_p] + [tmp] + intervals[e_p+1:]
        return res