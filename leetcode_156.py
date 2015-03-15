class Solution:
    UNIT_BIT = 9
    UNIT = 10 ** 9

    def to_int_list(self, s):
        r = []
        sl = len(s)
        si = sl
        while si > 0:
            s_start = si - Solution.UNIT_BIT
            r.append(long(s[s_start: si]))
            si = s_start
        return r

    def to_str(self, l):
        r = ''
        for e in l:
            r = str(e) + r
        zero_i = 0
        for e in r:
            if e == '0':
                zero_i += 1
            else:
                break
        r = r[zero_i:]
        return r

    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, a, b):
        x = self.to_int_list(a)
        y = self.to_int_list(b)
        xl = len(x)
        yl = len(y)
        z = [0 for i in xrange(xl + yl)]
        for i in xrange(xl):
            for j in xrange(yl):
                z[i + j] += x[i] * y[j]
                if z[i + j] >= Solution.UNIT:
                    z[i + j + 1] += z[i + j] / Solution.UNIT
                    z[i + j] = z[i + j] % Solution.UNIT
        return self.to_str(z)

s = Solution()
#print s.to_int_list("123456789123456788")
#print s.to_str([123456788, 123456789])
print s.multiply("123456789123456788", "123456789")