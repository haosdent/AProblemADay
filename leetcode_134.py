class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):                
        m = len(matrix)
        if matrix is None or m == 0:
            return 0

        n = len(matrix[0])
        h = [0 for x in range(n)]
        l = [0 for x in range(n)]
        r = [n for x in range(n)]

        ret = 0
        for i in range(m):
            left = 0
            right = n
            for j in range(n):
                if matrix[i][j] == '1':
                    h[j] += 1
                    l[j] = max(l[j], left)
                else:
                    left = j + 1
                    h[j] = 0
                    l[j] = 0
                    r[j] = n

            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    r[j] = min(r[j], right)
                    ret = max(ret, h[j] * (r[j] - l[j]))
                else:
                    right = j
        return ret

s = Solution()
A = [
    "11111111",
    "11111110",
    "11111110",
    "11111000",
    "01111000"
]
print s.maximalRectangle(A)
