# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        dic = {}
        res = 0
        room = 0
        intervals.sort(key=lambda x: x.start)
        for i in intervals:
            if i.start in dic:
                dic[i.start] += 1
            else:
                dic[i.start] = 1
            if i.end in dic:
                dic[i.end] -= 1
            else:
                dic[i.end] = -1
        for i in dic:
            res = max(res, room + dic[i])
        return res
