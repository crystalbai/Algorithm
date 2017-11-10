class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        pos_A = []
        pos_B = []
        res = [[0 for i in range(len(B[0]))] for j in range(len(A))]
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                if A[i][j] != 0:
                    pos_A.append([i, j])
        for i in xrange(len(B)):
            for j in xrange(len(B[0])):
                if B[i][j] != 0:
                    pos_B.append([i, j])
        for i in pos_A:
            if reversed(i) in pos_B:
                    res[i[0]][j[1]] += A[i[0]][i[1]] * B[j[0]][j[1]]
        return res
sol = Solution()
A, B = [[1,0,0],[-1,0,3]],[[7,0,0],[0,0,0],[0,0,1]]
print sol.multiply(A,B)