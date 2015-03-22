class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dic):
        f = [False for x in xrange(len(s) + 1)]
        f[0] = True
        for i in xrange(len(s) + 1):
            for j in xrange(i):
                if f[j] and s[j:i] in dic:
                    f[i] = True
                    break
        return f[len(s)]


s = Solution()
print s.wordBreak("leetcode", ["leet", "code"])