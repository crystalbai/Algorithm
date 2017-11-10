# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        timelist = []
        for inter in intervals:
            timelist.append((inter.start, 1))
            timelist.append((inter.end, -1))
        rooms = 0 ;maxrooms = 0
        timelist = sorted(timelist, key = lambda x: (x[0],x[1]))
        for i in timelist:
            rooms = rooms + i[1]
            maxrooms = max(maxrooms, rooms)
        return maxrooms

sol = Solution()
l = []
l.append(Interval(13,15))
l.append(Interval(1,13))
# l.append(Interval(15,20))
res = sol.minMeetingRooms(l)
print res
