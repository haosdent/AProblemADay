class Solution:
    # @return an integer
    def romanToInt(self, s):
        romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	result = 0
	for i in range(len(s)):
	  if i > 0 and romanMap[s[i]] > romanMap[s[i - 1]]:
	    result += int(romanMap[s[i]] - 2 * romanMap[s[i - 1]])
	  else:
	    result += int(romanMap[s[i]])

	return result

s = Solution()
print s.romanToInt('II')
