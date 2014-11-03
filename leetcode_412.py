class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        lefts = []
        maxLen = 0
        last = -1
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                lefts.append(i)
            elif c == ')':
                if len(lefts) == 0:
                    last = i
                else:
                    lefts.pop()
                    if len(lefts) == 0:
                        maxLen = max(maxLen, i - last)
                    else:
                        maxLen = max(maxLen, i - lefts[len(lefts) - 1])
        return maxLen

s = Solution()
print s.longestValidParentheses('()())')
print s.longestValidParentheses('()(()')
print s.longestValidParentheses('()(())')
