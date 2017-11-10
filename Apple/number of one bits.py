class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += n%2
            n= n >>1
        return res
sol = Solution()
print sol.hammingWeight(11)