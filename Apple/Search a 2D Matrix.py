class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        if target>matrix[-1][-1] or target< matrix[0][0]:
            return False
        else:
            f = 0
            rol = 0
            l = len(matrix)-1
            while l> f:
                rol = int((f+l)/2)
                if matrix[rol][-1]< target:
                    f = rol+1
                else:
                    l = rol
            lift = 0
            rol = l
            right = len(matrix[0])-1
            while lift <= right:
                col = int((lift+right)/2)
                if matrix[rol][col] == target:
                    return True
                if matrix[rol][col] < target:
                    lift = col+1
                else:
                    right = col-1
        return False

sol = Solution()
print sol.searchMatrix(
    [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
,3)
