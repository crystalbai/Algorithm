class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            res = chr((n-1)%26 + ord('A'))+res
            n = int((n-1)/26)
        return res
sol = Solution()
print sol.convertToTitle(26)
