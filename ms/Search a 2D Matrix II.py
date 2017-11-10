import numpy as np
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) ==0:
            return False
        matrix = np.array(matrix,ndmin = 2)
        l_row, r_row = 0, matrix.shape[0] - 1
        l_col, r_col = 0, matrix.shape[1] - 1

        while l_row <= r_row and l_col <= r_col:
            mid_row = (l_row + r_row) / 2
            mid_col = (l_col + r_col) / 2
            if matrix[mid_row][mid_col] == target:
                return True
            if matrix[mid_row][mid_col] < target:
                tmp = self.searchMatrix(matrix[mid_row + 1:,mid_col:], target)
                if tmp == True:
                    return tmp
                return self.searchMatrix( matrix[:,mid_col + 1:], target)
            if matrix[mid_row][mid_col] > target:
                if r_row ==0 and r_col ==0:
                    return bool(matrix[mid_row][mid_col] == target)
                return self.searchMatrix( matrix[:mid_row+1,:mid_col+1], target)
        return False
sol = Solution()
print sol.searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],
5)
print type(sol.searchMatrix([[-5]], -10))