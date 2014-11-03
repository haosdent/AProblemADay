class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
	preR = 0
        r = 0
	for i in range(len(s)):
	  if s[i] == ' ':
	    preR = r
	    r = 0
	  else:
	    r += 1
	return r

s = Solution()
print s.lengthOfLastWord('Hello world')
print s.lengthOfLastWord('a ')
print s.lengthOfLastWord('a            b   ')
