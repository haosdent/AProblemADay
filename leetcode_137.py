class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        l = len(s1)
        if len(s1) != len(s2):
            return False
        f = [[[False for z in xrange(l)] for y in xrange(l)] for x in xrange(l + 1)]

        for i in xrange(l):
            for j in xrange(l):
                f[1][i][j] = s1[i] == s2[j]

        for i in xrange(1, l + 1):
            for j in xrange(l - i):
                for k in xrange()
