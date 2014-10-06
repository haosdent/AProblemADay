class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]
        l_a = len(a)
        l_b = len(b)
        l = max(l_a, l_b)
        d = 0
        r = ''
        for i in range(l):
            s = d
            if i < l_a:
                s += int(a[i])
            if i < l_b:
                s += int(b[i])
            d = s / 2
            r += str(s % 2)
        if d > 0:
            r += str(d)

        return r[::-1]


s = Solution()
print s.addBinary('111', '1')
