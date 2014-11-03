class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        splits = path.split('/')
	result = []
	for s in splits:
	  if s == '' or s == '.':
	    pass
	  elif s == '..' and len(result) > 0:
	    result.pop()
	  elif s != '..':
	    result.append(s)
	return '/' + '/'.join(result)


s = Solution()
print s.simplifyPath('/a/./b/../../c/')
print s.simplifyPath('/..')
