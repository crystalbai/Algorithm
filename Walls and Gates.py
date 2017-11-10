import numpy
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i,j, 0)

    def dfs(self, rooms, i,j, val):
        if i < 0 or j < 0 or i >= len(rooms) or j >= len(rooms[0]) or val > rooms[i][j]:
            return

        rooms[i][j] = val
        self.dfs(rooms, i-1,j, val+1)
        self.dfs(rooms, i + 1, j, val + 1)
        self.dfs(rooms, i, j-1, val + 1)
        self.dfs(rooms, i, j+1, val + 1)

sol = Solution()
a = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
sol.wallsAndGates(a)
print a