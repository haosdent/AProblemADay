class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)

        if n < 2:
            return 0
        
        f = [0 for x in range(n)]
        g = [0 for x in range(n)]

        v = prices[0]
        p = prices[n - 1]
        for i in range(1, n, 1):
            v = min(v, prices[i])
            f[i] = max(f[i - 1], prices[i] - v)

        for i in range(n - 2, -1, -1):
            p = max(p, prices[i])
            g[i] = max(g[i + 1], p - prices[i])

        m = 0
        for i in range(n):
            m = max(m, f[i] + g[i])

        return m


s = Solution()
print s.maxProfit([1, 2])
