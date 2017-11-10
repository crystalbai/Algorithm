import copy
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        self.dir = [[-1,0],[1,0],[0,-1],[0,1]]
        dp = copy.deepcopy(maze)
        return self.dfs(maze, start, destination, dp, [0,0])

    def dfs(self, maze, start, destination, dp, d_pre):
        next_pos = start[0]+d_pre[0],start[1]+d_pre[1]
        if start == destination and ((not self.is_val(maze, next_pos)) or maze[next_pos[0]][next_pos[1]] == 1):
            return True
        dp[start[0]][start[1]] = -1
        tmp_res = False
        for d in self.dir:
            cur_pos = [0,0]
            d_pre = d
            cur_pos[0],cur_pos[1] = start[0]+d[0],start[1]+d[1]
            if self.is_val(maze, cur_pos) and dp[cur_pos[0]][cur_pos[1]] == 0:
                tmp_res = tmp_res or self.dfs(maze, cur_pos, destination,dp, d_pre)
        return tmp_res

    def is_val(self, maze, pos):
        if pos[0] < len(maze) and pos[0]>= 0 and pos[1]< len(maze[0]) and pos[1]>= 0:
            return True
        else:
            return False
sol = Solution()
print sol.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
[0,4],
[1,2])