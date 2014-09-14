class Solution:
    # @param s, a string
    # @return an integer    
    def getIsPalindrome(self, s):
        l = len(s)
        m = [[False for x in xrange(l)] for x in xrange(l)]
        
        for i in xrange(l):
            m[i][i] = True;            
        for i in xrange(2, l + 1):
            for j in xrange(0, l - i + 1):                
                if i == 2:
                    m[j][j + i - 1] = s[j] == s[j + i - 1]
                else:
                    m[j][j + i - 1] = m[j + 1][j + i - 2] and s[j] == s[j + i - 1]                

        return m

    def minCut(self, s):
        if s is None or len(s) == 0:
            return 0

        l = len(s)
        cut = [l for x in xrange(l + 1)]
        isPalindrome = self.getIsPalindrome(s)
        cut[0] = 0

        for i in xrange(1, l + 1):
            for j in xrange(1, i + 1):
                if isPalindrome[i - j][i - 1] and cut[i - j] != l:
                    cut[i] = min(cut[i], cut[i - j] + 1)
        return cut[l] - 1
   
