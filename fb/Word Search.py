import numpy as np
from operator import add
class Solution(object):
    def __init__(self):

        self.selfdirec = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    isVisit = np.zeros([len(board), len(board[0])])
                    isVisit[i][j] = 1
                    if self.dfs([i,j], board, word[1:], isVisit):
                        return True
        return False


    def dfs(self, cur_pos, board, res_word, isVisit):
        for d in self.selfdirec:
            tmp_loc = map(add, d, cur_pos)
            if tmp_loc[0] < 0 or tmp_loc[0] >= len(board) or tmp_loc[1] < 0 or tmp_loc[1]>= len(board[0]):
                continue
            if board[tmp_loc[0]][tmp_loc[1]] == res_word[0] and isVisit[tmp_loc[0]][tmp_loc[1]] == 0:
                if len(res_word) == 1:
                    return True
                isVisit[tmp_loc[0]][tmp_loc[1]] = 1
                if self.dfs(tmp_loc, board, res_word[1:], isVisit):
                    return True
                isVisit[tmp_loc[0]][tmp_loc[1]] = 0
        return False



sol = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','E','S'],
  ['A','D','E','E']
]
word = "ABCEFSADEESE"
print sol.exist(board, word)
