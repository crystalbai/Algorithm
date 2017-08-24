# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals_cp = sorted(intervals, key = lambda i: (i.start, i.end))
        max_tail = intervals_cp[0].end
        for i in intervals_cp[1:]:
            if i.start < max_tail:
                return False
        return True
