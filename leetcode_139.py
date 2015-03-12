class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)

        if n == 0:
            return m
        elif m == 0:
            return n

        f = [[0 for x in xrange(n + 1)] for y in xrange(m + 1)]

        for i in xrange(n + 1):
            f[0][i] = i
        for i in xrange(m + 1):
            f[i][0] = i

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if word1[j - 1] == word2[i - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i][j - 1], f[i - 1][j]) + 1

        return f[m][n]

s = Solution()
print s.minDistance('', '')
print s.minDistance('abc', 'abc')
print s.minDistance('abc', 'abcd')
print s.minDistance('sea', 'eat')