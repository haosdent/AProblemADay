class Solution:
    # @param s, a string
    # @return an integer
    # f[n] = f[n - 1] + f[n - 2] || f[n - 1]
    def numDecodings(self, s):
        prev = 0
        cur = 1
        l = len(s)
        if l == 0:
            return 0

        for i in xrange(1, l + 1):
            if i <= 1:
                prev = 0
            elif s[i - 1] > 6 and s[i - 2] > 1:
                prev = 0
            elif s[i - 2] > 2:
                prev = 0
            tmp = cur
            cur += prev
            prev = tmp

        return cur

s = Solution()
print s.numDecodings([1, 2])

