class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x
        if x == 1:
            return 1
        while l < r:
            ans = int((l + r) / 2)
            if ans ** 2 == x:
                return ans
            elif ans ** 2 > x:
                r = ans-1
            else:
                l = ans+1
        return -1
sol = Solution()
print sol.mySqrt(2)