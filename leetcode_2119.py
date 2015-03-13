class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        a = False
        b = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                a = True

        for j in range(n):
            if matrix[0][j] == 0:
                b = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if a:
            for i in range(m):
                matrix[i][0] = 0

        if b:
            for j in range(n):
                matrix[0][j] = 0

        return matrix

s = Solution()
print s.setZeroes([[0, 1], [1, 2]])
