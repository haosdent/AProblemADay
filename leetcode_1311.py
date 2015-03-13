class Solution:
    def numDistinct(self, s, t):
        f = [0 for x in xrange(len(t) + 1)]
        f[0] = 1
        for i in xrange(len(s)):
            for j in xrange(len(t) - 1, -1, -1):
                print "S[%d]: %s, T[%d]: %s, f[%d]: %d" % (i, s[i], j, t[j], j, f[j])
                if s[i] == t[j]:
                    f[j + 1] += f[j]

        return f[len(t)]

s = Solution()
#print s.numDistinct("rabbbit", "rabbit")
print s.numDistinct("ab", "cd")