class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
	for c in s:
	  if len(stack) > 0:
       	    tmp = stack[len(stack) - 1]
	  else:
	    tmp = None
	  if c == '(' or c == '[' or c == '{':
	    stack.append(c)
	  elif c == ')':
	    if tmp != '(':
	      return False 
	    else:
	      stack.pop()
	  elif c == ']':
	    if tmp != '[':
	      return False
	    else:
	      stack.pop()
	  elif c == '}':
	    if tmp != '{':
	      return False
	    else:
	      stack.pop()

	return len(stack) == 0

s = Solution()
print s.isValid('()')
print s.isValid('()[]{}')
print s.isValid('(]')
print s.isValid('([)]')
