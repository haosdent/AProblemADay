class Solution:
    # @return a string
    def convert(self, s, nRows):
        sl = len(s)
        if nRows <= 1 or sl <= 1:
            return s
        result = ""
        for i in xrange(nRows):
            for j in xrange(i, sl, nRows * 2 - 2):
                result += s[j]
                tmp_i = j + (nRows - i - 1) * 2
                if j < tmp_i and tmp_i < j + nRows * 2 - 2 and tmp_i < sl:
                    result += s[tmp_i]
        return result


s = Solution()
print s.convert("PAYPALISHIRING", 3)