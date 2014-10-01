class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        prev = 0
        cur = 1
        for i in range(n):
            tmp = cur
            cur += prev
            prev = tmp
        return cur

        
s = Solution()
print s.climbStairs(1)
print s.climbStairs(2)
print s.climbStairs(3)
print s.climbStairs(4)
