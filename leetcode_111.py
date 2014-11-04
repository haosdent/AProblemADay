class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if x == 0:
            return 0
        if n < 0:
            return 1 / self.pow(x, -n)
        elif n == 0:
            return 1
        else:
            v = self.pow(x, n / 2)
            t = 1
            if n % 2 == 1:
                t = x
            return v * v * t


s = Solution()
print s.pow(2, 4)
