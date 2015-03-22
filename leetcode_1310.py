class Solution:
    # @param s, a string
    # @return an integer
    # f[n] = f[n - 1] + f[n - 2] || f[n - 1]
    def numDecodings(self, s):
        prev = 0
        cur = 1
        l = len(s)
        if l == 0 or s[0] == '0':
            return 0

        for i in xrange(1, l + 1):
            if s[i - 1] == '0':
                cur = 0

            if i <= 1:
                prev = 0
            elif ord(s[i - 1]) > ord('6') and ord(s[i - 2]) > ord('1'):
                prev = 0
            elif ord(s[i - 2]) > ord('2'):
                prev = 0

            tmp = cur
            cur += prev
            prev = tmp

        return cur

s = Solution()
#print s.numDecodings("12")
#print s.numDecodings("0")
#print s.numDecodings("10")
#print s.numDecodings("01")
print s.numDecodings("10012")
#print s.numDecodings("101")
print s.numDecodings("110")

