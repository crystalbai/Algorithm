class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans = 0
        if len(board) == 0:
            return 0
        for i in len(range(board)):
            for j in len(range(board[0])):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j]== '.')and (j == 0 or board[i][j-1] == '.'):
                    ans +=1

        return ans