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
        while s_i < s_l:
            if p_i >= p_l or (p[p_i] != s[s_i] and p[p_i] != '*' and p[p_i] != '?'):
                if star:
                    s_p += 1
                    s_i = s_p
                    p_i = p_p
                else:
                    break
            elif p[p_i] == '*':
                while p_i < p_l and p[p_i] == '*':
                    star = True
                    p_i += 1
                    p_p = p_i
                    s_p = s_i
            elif p[p_i] == s[s_i] or p[p_i] == '?':
                p_i += 1
                s_i += 1
        while p_i < p_l and p[p_i] == '*':
            p_i += 1
        return p_i == p_l and s_i == s_l


s = Solution()
print s.isMatch('aa', '*')
print s.isMatch('aa', 'a')
print s.isMatch('aa', '*?*?*?*')
print s.isMatch('', '*')
