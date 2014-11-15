class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) < 1:
            return None
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]


s = Solution()
print s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
print s.minimumTotal([])
print s.minimumTotal([[1]])
    
