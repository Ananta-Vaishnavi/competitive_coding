class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, i, j, k):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return False
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        temp = board[i][j]
        board[i][j] = '#'
        found = self.dfs(board, word, i+1, j, k+1) or self.dfs(board, word, i-1, j, k+1) or self.dfs(board, word, i, j+1, k+1) or self.dfs(board, word, i, j-1, k+1)
        board[i][j] = temp
        return found
