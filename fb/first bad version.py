# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version > 6:
        return True
    else:
        return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.searchBad(1,n)

    def searchBad(self,s,e):
        mid = int((s+ e) / 2)

        if isBadVersion(mid):
            if isBadVersion(mid - 1) == False:
                return mid
            else:
                if mid >= e:
                    return False
                return self.searchBad(s,mid)
        else:
            return self.searchBad(mid+1, e)


sol = Solution()
res = sol.firstBadVersion(9)
print res