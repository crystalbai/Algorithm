class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """

        self.M = [[0 for i in range(n)] for j in range(n)]
        self.n = n

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
        self.M[row][col] = player
        is_true = [True] * 4
        for i in range(self.n):
            if self.M[i][i] != player:
                is_true[0] = False
            if self.M[i][self.n - 1 - i] != player:
                is_true[1] = False
            if self.M[i][col] != player:
                is_true[2] = False
            if self.M[row][i] != player:
                is_true[3] = False
        return player if max(is_true) != 0 else 0




        # Your TicTacToe object will be instantiated and called as such:
n = 2
obj = TicTacToe(n)
param_1 = obj.move(0,1,1)
param_1 = obj.move(1,1,2)
param_1 = obj.move(1,0,1)
print param_1