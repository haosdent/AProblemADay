class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        n = len(s1)
        m = len(s2)
        f = [[True for y in range(m + 1)] for x in range(n + 1)]
        for j in range(m):
            f[0][j + 1] = s2[j] == s3[j] and f[0][j]
        for i in range(n):
            f[i + 1][0] = s1[i] == s3[i] and f[i][0]
        for i in range(n):
            for j in range(m):
                f[i + 1][j + 1] = (s1[i] == s3[i + j + 1] and f[i][j + 1]) or (s2[j] == s3[i + j + 1] and f[i + 1][j])

        return f[n][m]


s = Solution()
print s.isInterleave("a", "b", "bb")
#print s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
A = [
    [True, True],
    [False, True]
]
