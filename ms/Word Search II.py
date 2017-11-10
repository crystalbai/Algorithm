import copy
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        def dfs(board, words, pos_x, pos_y, is_visit):
            direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            if words == "":
                return True
            if words == board[pos_x][pos_y]:
                return True
            visit = copy.deepcopy(is_visit)
            visit[pos_x][pos_y] = True
            if words[0] == board[pos_x][pos_y]:
                for d in direc:
                    x = pos_x + d[0]
                    y = pos_y + d[1]
                    if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and not visit[x][y] and (len(words) == 1 or board[x][y]== words[1]):
                        if dfs(board, words[1:], x, y, visit):
                            return True
            return False

        res = []
        words = set(words)
        for w in words:
            find = False
            is_visit = [[False for i in range(len(board[0]))] for j in range(len(board))]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if w[0] == board[i][j]:
                        if dfs(board, w, i, j, is_visit):
                            find = True
                            res.append(w)
                    if find:
                        break
                if find:
                    break
        return res



sol = Solution()
board = []
l = ["oaan","etae","ihkr","iflv"]
for i in l:
    board.append(list(i))
print sol.findWords([['a','a']],['a','a'])