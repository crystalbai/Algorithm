import numpy as np
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = np.zeros([len(A), len(B[0])], dtype = int)
        A = np.asarray(A)
        B = np.asarray(B)
        for i in xrange(len(A)):
            idx = np.where(A[i]!= 0)[0]
            for iter in idx:
                idx_b = np.where(B[iter, :]!= 0)
                for j in idx_b:
                    ans[i][j] = ans[i][j] + A[i,iter] * B[iter,j]
        return ans.tolist()
sol = Solution()
ans = sol.multiply([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]])
print ans
