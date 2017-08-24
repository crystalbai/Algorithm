# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    if b == 3:
        return True
    else:
        return False

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(1,n):
            if knows(candidate,i):
                candidate = i
        for i in range(n):
            if candidate == i:
                continue
            else:
                if knows(i, candidate) == False or knows(candidate,i) == True:
                    return -1
        return candidate

sol = Solution()
res = sol.findCelebrity(10)
print res