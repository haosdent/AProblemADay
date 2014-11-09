class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        cur_min = 9223372036854775807
        for price in prices:
            profit = max(profit, price - cur_min)
            cur_min = min(cur_min, price)

        return profit


s = Solution()
print s.maxProfit([300, 302, 100, 200])
