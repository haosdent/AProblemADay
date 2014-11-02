class Solution:
    # @return a string
    def countAndSay(self, n):
        oldStr = '1'
	for i in range(n, 0, -1):
	  newStr = ''
	  j = 0
	  while j < len(oldStr):
	    count = 1
	    while j + 1 < len(oldStr) and oldStr[j] == oldStr[j + 1]:
	      count += 1
	      j += 1
	    newStr += str(count) + oldStr[j]
	    j += 1    
	  oldStr = newStr

	return oldStr  


s = Solution()
print s.countAndSay(3)
