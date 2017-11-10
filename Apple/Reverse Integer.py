class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_sz = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    tmp_sz = max_sz+1
                    if self.isvalue(matrix, i,j, tmp_sz,matrix):
                        max_sz = tmp_sz
        return max_sz




    def isvalue(self,i,j,tmp_sz,matrix):
        for x in range(i, i+tmp_sz):
            for y in range(j,j+tmp_sz):
                if matrix[x][y]!= 1:
                    return False
        return True

sol = Solution()

