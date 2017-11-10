import math
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            return 1/self.myPow(x,-n)
        if n == 0 :
            return 1
        half = self.myPow(x, math.floor(n/2))
        if n%2 == 0:
            return half *half
        else:
            return half*half*x
sol = Solution()
print sol.myPow(8.88023,3)
