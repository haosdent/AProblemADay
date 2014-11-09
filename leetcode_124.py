class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        s = 0
        for i in range(1, len(prices)):
            if (prices[i] > prices[i - 1]):
                s += prices[i] - prices[i - 1]

        return s


s = Solution()
print s.maxProfit([300, 302, 100, 200])
