import numpy as np


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        vis = np.zeros([len(matrix), len(matrix[0])])
        res = []
        i = 0; j = 0

        while vis[i][min(j+1, len(matrix[0])-1)] !=1 or vis[max(i-1,0)][j]!=1 or vis[min(i+1, len(matrix)-1)][j]!=1 or vis[i][max(j-1,0)]!=1:
            if vis[i][j]==0:
                res.append(matrix[i][j])
                vis[i][j] =1
            while j+1 < len(matrix[0]) and vis[i][j + 1] == 0:
                j += 1
                res.append(matrix[i][j])
                vis[i, j] = 1

            while i+1 < len(matrix) and vis[i + 1][j] == 0:
                i += 1
                res.append(matrix[i][j])
                vis[i, j] = 1

            while j-1 >=0 and vis[i][j-1] == 0:
                j -= 1
                res.append(matrix[i][j])
                vis[i, j] = 1

            while i-1 >= 0 and vis[i-1][j] == 0 :
                i -= 1
                res.append(matrix[i][j])
                vis[i, j] = 1

        return res




sol = Solution()
print sol.spiralOrder([[1,2, 3,  4],
                       [5,6 ,7,  8],
                       [9,10,11,12],
                       [13,14,15,16]])
print sol.spiralOrder([[1]])