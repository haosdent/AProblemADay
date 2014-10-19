class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]

        most_right = len(strs[0])
        for i in range(1, len(strs)):
           for j in range(most_right):
               if j == len(strs[i]) or strs[i][j] != strs[i - 1][j]:
                   most_right = j
                   break

        return strs[0][0:most_right]


s = Solution()
print s.longestCommonPrefix(['12345', '1234', '123456'])
