class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def findAdjacent(i, j, word):
            if len(word) <= 1:
                return True

            board[i][j] = ""
            
            if i > 0 and board[i-1][j] == word[1]:
                if findAdjacent(i-1, j, word[1:]):
                    return True
            if i < len(board) - 1 and board[i+1][j] == word[1]:
                if findAdjacent(i+1, j, word[1:]):
                    return True

            if j > 0 and board[i][j-1] == word[1]:
                if findAdjacent(i, j-1, word[1:]):
                    return True
            if j < len(board[i]) - 1 and board[i][j+1] == word[1]:
                if findAdjacent(i, j+1, word[1:]):
                    return True
            
            board[i][j] = word[0]

            return False


        remainingWord = word
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if findAdjacent(i, j, word):
                        return True

        return False