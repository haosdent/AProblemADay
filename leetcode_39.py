class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
	stateMap = {'INVALID': 0, 'SPACE': 1, 'SIGN': 2, 'DIGIT': 3, 'DOT': 4, 'EXPONENT': 5, 'NUM_INPUTS': 6}
	transitionTable = [
	  [-1, 0, 3, 1, 2, -1],
	  [-1, 8, -1, 1, 4, 5],
	  [-1, -1, -1, 4, -1, -1],
	  [-1, -1, -1, 1, 2, -1],
	  [-1, 8, -1, 4, -1, 5],
	  [-1, -1, 6, 7, -1, -1],
	  [-1, -1, -1, 7, -1, -1],
	  [-1, 8, -1, 7, -1, -1],
	  [-1, 8, -1, -1, -1, -1] 
	]
	state = 0
	for c in s:
	  inputType = 0
	  if c >= '0' and c <= '9':
	    inputType = 3
	  elif c == '-' or c == '+':
	    inputType = 2
	  elif c == ' ':
	    inputType = 1
	  elif c == '.':
	    inputType = 4
	  elif c == 'e' or c == 'E':
	    inputType = 5
	  state = transitionTable[state][inputType]
	  if state == -1:
	    return False

	return state == 1 or state == 4 or state == 7 or state == 8
	  

s = Solution()
print s.isNumber('-1.')

