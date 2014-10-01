class Solution:
    # @return a list of integers
    def grayCode(self, n):
        size = 1 << n
        result = []
        for i in range(size):
            result.append(i ^ (i >> 1))

        return result

s = Solution()
print s.grayCode(4)
