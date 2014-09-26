class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        m = {}
        longest = 0
        for e in num:
            m[e] = False

        for e in num:
            if m[e]:
                continue

            m[e] = True
            l = 0
            i = e
            while m.has_key(i):
                m[i] = True
                i += 1
                l += 1
            i = e - 1
            while m.has_key(i):
                m[i] = True
                i -= 1
                l += 1

            if l > longest:
                longest = l

        return longest


s = Solution()
print s.longestConsecutive([2147483646,-2147483647])
