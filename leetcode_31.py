class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        tmp_s = ''
        for e in s:
            if e >= 'a' and e <= 'z':
                tmp_s += e
            elif e >= 'A' and e <= 'Z':
                tmp_s += e.lower()
            elif e >= '0' and e <= '9':
                tmp_s += e
        i = 0
        j = len(tmp_s) - 1
        result = True
        while i < j:
            if tmp_s[i] != tmp_s[j]:
                result = False
                break
            i += 1
            j -= 1
        return result

s = Solution()
print s.isPalindrome('1a2')


