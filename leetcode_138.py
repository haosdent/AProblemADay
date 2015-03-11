class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        if m > 0:
            n = len(grid[0])
        else:
            return 0

        f = [[0 for x in xrange(n)] for y in xrange(m)]
        for j in xrange(m):
            for i in xrange(n):
                if i == 0 and j == 0:
                    f[j][i] = grid[j][i]
                elif i == 0:
                    f[j][i] = f[j - 1][i] + grid[j][i]
                elif j == 0:
                    f[j][i] = f[j][i - 1] + grid[j][i]
                else:
                    f[j][i] = min(f[j - 1][i], f[j][i - 1]) + grid[j][i]

        return f[m - 1][n - 1]


s = Solution()
grid = [[1, 2, 5], [3, 4, 7]]
print s.minPathSum(grid)