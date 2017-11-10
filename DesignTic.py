class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid = [[0 for i in range(n)] for j in range(n)]
        self.n = n
        self.grid = [[0,0],[0,0]]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.grid[row][col] = player
        ## check for win
        res = True
        for i in range(0, self.n):
            if self.grid[row][i] != player:
                res = False
                break
        if res == True:
            return player
        res = True
        for i in range(0, self.n):
            if self.grid[i][col] != player:
                res = False
                break
        if res == True:
            return player

        if col == row:
            res = True
            for i in range(self.n):
                if self.grid[i][i] != player:
                    res = False
                    break
        if res == True:
            return player

        if col == self.n - 1 - row:
            res = True
            for i in range(self.n):
                if self.grid[i][self.n - 1 - i] != player:
                    res = False
                    break
        return player if res == True else 0

# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(2)
print  obj.move(1,1,2)