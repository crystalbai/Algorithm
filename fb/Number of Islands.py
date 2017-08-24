import numpy as np
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        grid = list(grid)
        if len(grid) == 0:
            return 0
        m = np.zeros((len(grid), len(grid[0])))
        count =0
        #dfs
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                   count+=1
                   self.dfs(grid,i,j)
        return count

    def dfs(self, grid, i,j):
        if i>= 0 and i <len(grid) and j >= 0 and j < len(grid[0]):

            if grid[i][j] == '1':
                grid[i][j] = '2'
                self.dfs(grid, i-1,j)
                self.dfs(grid, i+1, j)
                self.dfs(grid, i, j-1)
                self.dfs(grid, i, j+1)





sol = Solution()
# grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
# grid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
grid = [list("111"),list("010"),list("111")]
res = sol.numIslands(grid)
print res