class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):

        for i in range(9):
            visited = [False for x in range(9)]
            for j in range(9):
                if self.is_used(visited, board[i][j]):
                    return False
                
        for i in range(9):
            visited = [False for x in range(9)]
            for j in range(9):
                if self.is_used(visited, board[j][i]):
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                visited = [False for x in range(9)]
                for k in range(9):
                    if self.is_used(visited, board[i + k / 3][j + k % 3]):
                        return False

        return True

    def is_used(self, visited, digit):
        if digit == '.':
            return False

        digit = int(digit)
        if digit < 0 or digit > 9 or visited[digit - 1]:
            return True

        visited[digit - 1] = True

        return False


s = Solution()
print s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
