class Solution(object):
    def checkNeighbor(self, i, j, m, n, board):
        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        cnt = 0
        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]
            if nx >= 0 and ny >= 0 and nx < m and ny < n and (board[nx][ny] == 1 or board[nx][ny] == 2 or board[nx][ny] == 4):
                cnt += 1
        return cnt

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.checkNeighbor(i, j, m, n, board) == 3:
                    if board[i][j] == 0:
                        board[i][j] = 3
                if self.checkNeighbor(i, j, m, n, board) > 3:
                    if board[i][j] == 1:
                        board[i][j] = 4
                if self.checkNeighbor(i, j, m, n, board) < 2:
                    if board[i][j] == 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] %= 2
        print board



sol = Solution()
sol.gameOfLife([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
