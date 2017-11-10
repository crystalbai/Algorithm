class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1], [1, 1]]
        if numRows < 2:
            return res[:numRows]
        for i in range(numRows - 1):
            tmp = []
            for j in range(len(res[-1]) - 1):
                tmp.append(res[-1][j] + res[-1][j + 1])
            tmp.append(1)
            tmp.insert(0, 1)
            res.append(tmp)
        return res


sol = Solution()
print sol.generate(2)