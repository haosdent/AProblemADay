class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        left = 0
        right = x
        while left < right:
            mid = left + (right - left) / 2
            if left == mid:
                if x / right != right:
                    return left
                else:
                    return right
            tmp = x / mid
            if tmp > mid:
                left = mid
            else:
                right = mid

        return left


s = Solution()
print s.sqrt(4)
print s.sqrt(5)
print s.sqrt(6)
print s.sqrt(7)
print s.sqrt(8)
print s.sqrt(9)
