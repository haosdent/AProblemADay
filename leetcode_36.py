class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        s_p = 0
        p_p = 0
        s_i = 0
        p_i = 0
        p_l = len(p)
        s_l = len(s)
        star = False
        while p_i < p_l:
            if p[p_i] == '*':
                while p_i < p_l and p[p_i] == '*':
                    star = True
                    p_i += 1
                    p_p = p_i
                    s_p = s_i
                if p_i == p_l:
                    return True
            elif p[p_i] == s[s_i] or p[p_i] == '?':
                p_i += 1
                s_i += 1
            elif p[p_i] != s[s_i]:
                if star:
                    s_p += 1
                    s_i = s_p
                    p_i = p_p
                else:
                    break
        return p_i == p_l and s_i == s_l


s = Solution()
print s.isMatch('aab', '?*b')
