class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        for idx, c in enumerate(citations):
            if c >= len(citations)-idx:
                return len(citations)-idx

sol = Solution()
print sol.hIndex()