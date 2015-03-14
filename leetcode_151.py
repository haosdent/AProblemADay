class Solution:
    def reverse(self, x):
        r = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x > 0:
            r = r * 10 + x % 10
            x /= 10
        return r * sign

s = Solution()
print s.reverse(1234)
print s.reverse(1234000)
print s.reverse(-1234)