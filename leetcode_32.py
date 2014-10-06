class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        h_len = len(haystack)
        n_len = len(needle)
        x = h_len - n_len + 1
        if (x < 1):
            return None
        result = True
        pivot = 0
        for i in range(x):
            result = True
            for j in range(n_len):
                if needle[j] != haystack[i + j]:
                    result = False
                    break
            if result:
                pivot = i
                break
        if result:
            return haystack[pivot:]
        else:
            return None


s = Solution()
print s.strStr('hello', 'e')
