class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        l = len(s1)
        if len(s1) != len(s2):
            return False
        f = [[[False for z in xrange(l)] for y in xrange(l)] for x in xrange(l + 1)]
