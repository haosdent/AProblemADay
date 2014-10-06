class Solution:
    # @return a string
    def longestPalindromeDp(self, s):
        max_len = 1
        start = 0
        l = len(s)
        flag = [[False for x in range(l)] for y in range(l)]
        for i in range(len(s)):
            flag[i][i] = True
            for j in range(i):
                if (j == i - 1 or flag[j + 1][i - 1]) and s[j] == s[i]:
                    flag[j][i] = True
                    tmp_len = i - j + 1
                    if tmp_len > max_len:
                        max_len = tmp_len
                        start = j
                else:
                    flag[j][i] = False

        return s[start:start + max_len]

    def longestPalindrome(self, s):
        if s == '':
            return s
        origin_s = s
        s = ''
        for c in origin_s:
            s += '#'
            s += c
        if s != '':
            s += '#'

        max_edge = 0
        center = 0

        # assume s is #a#b#c# here
        l = len(s)
        p = [0 for x in range(l)]
        for i in range(l):
            i_mirror = 2 * center - i
            p[i] = min(max_edge - i, p[i_mirror])
            while i - 1 - p[i] >= 0 and i + 1 + p[i] < l and s[i + 1 + p[i]] == s[i - 1 - p[i]]:
                p[i] += 1
            edge = i + p[i]
            if edge > max_edge:
                max_edge = edge
                center = i

        index = 0
        max_p = 0
        for i in range(len(p)):
            if p[i] > max_p:
                max_p = p[i]
                index = i
        start = (index - max_p) / 2
        end = start + max_p
        return origin_s[start:end]


s = Solution()
print s.longestPalindrome('hello')
#print s.longestPalindrome('dqlvtrcystnncxjffjrkiiqgtcunbwntqrpqkjepzbxzodeckrbrwzjjuptloypmjgbwioqtjzjjgqpaemgvxkapjgbfhhwltvtqgkozuzvlwetftjeocjqrdwlhdwtgzdhwvmuhvmdpkxnzrrizjntxbbpzwtjryecgfajolalwdzxqtknvvvaxuhanzowlbwjraigvrflcqoormbeexekmqpmuuobseumctsiwhvdohywjaylixqgqookgneokebtmoyaspnzbwqzffyocvcylcjobnzbmhsdprzrgdlyzuutyuwygzeldfewicjnukguisceeopckkoviayrcqanzsryhwqhxjxcpiejojztrxad')
