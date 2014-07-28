class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        total = 0
        p = 0
        index = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            p += diff
            total += diff
            if p < 0:
                p = 0
                index = i + 1
        if total >= 0:
            return index
        else:
            return -1
        
if __name__ == "__main__":
    s = Solution()
    print s.canCompleteCircuit([2], [2])
