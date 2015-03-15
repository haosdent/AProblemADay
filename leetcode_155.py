class Solution:
    # @return a string
    def minWindow(self, s, t):
        sl = len(s)
        tl = len(t)
        if sl == 0 or sl < tl:
            return ""

        ascii_size = 256
        appear_count = [0 for x in xrange(ascii_size)]
        expected_count = [0 for x in xrange(ascii_size)]
        for c in t:
            expected_count[ord(c)] += 1
        appear_size = 0

        appear_start = 0
        appear_end = 0
        int_max = 100000000000
        min_win = int_max
        win_start = 0
        for win_end, sc in enumerate(s):
            if expected_count[ord(sc)] > 0:
                appear_count[ord(sc)] += 1
                if appear_count[ord(sc)] <= expected_count[ord(sc)]:
                    appear_size += 1
            if appear_size == tl:
                while (appear_count[ord(s[win_start])] > expected_count[ord(s[win_start])]) or (expected_count[ord(s[win_start])] == 0):
                    appear_count[ord(s[win_start])] -= 1
                    win_start += 1
                current_win = win_end - win_start + 1
                if current_win < min_win:
                    min_win = current_win
                    min_start = win_start
        if min_win == int_max:
            return ""
        else:
            return s[min_start:min_start + min_win]


s = Solution()
print s.minWindow("CACBAB", "AB")
print s.minWindow("ADOBECODEBANC", "ABC")

