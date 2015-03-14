class Solution:
    def numDistinct(self, s, t):
        sl = len(s)
        tl = len(t)
        f = [[0 for x in xrange(tl + 1)] for y in xrange(sl + 1)]
        for i in xrange(tl + 1):
            f[0][i] = 0
        for i in xrange(sl + 1):
            f[i][0] = 1

        for i in xrange(1, sl + 1):
            for j in xrange(1, min(i + 1, tl + 1)):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j]
        return f[sl][tl]

s = Solution()
print s.numDistinct("rabbbit", "rabbit")
print s.numDistinct("abb", "ab")