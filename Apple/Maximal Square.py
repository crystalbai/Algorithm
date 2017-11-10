class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == [] or max(max(matrix)) == '0':
            return 0
        max_sz = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != '0':
                    tmp_sz = max_sz+1
                    while self.isvalue(matrix, i,j, tmp_sz):
                        max_sz = tmp_sz
                        tmp_sz +=1
        return max_sz**2




    def isvalue(self,matrix,i,j,tmp_sz):
        if i+tmp_sz > len(matrix) or j + tmp_sz> len(matrix[0]):
            return False
        for x in range(i, i+tmp_sz):
            for y in range(j,j+tmp_sz):
                if matrix[x][y]!= '1':
                    return False
        return True

sol = Solution()
l = ["11100","11100","11111","01111","01111","01111"]
a = []
for i in l:
    a.append(list(i))
print sol.maximalSquare(a)