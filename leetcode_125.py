class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        m = {}
        max_len = 0
        start = 0
        i = 0
        for i in range(len(s)):
            if s[i] in m and m[s[i]] >= start:
                max_len = max(max_len, i - start)
                start = m[s[i]] + 1
            m[s[i]] = i
        max_len = max(max_len, len(s) - start)
        return max_len


s = Solution()
print s.lengthOfLongestSubstring("qopubjguxhxdipfzwswybgfylqvjzhar")
#print s.lengthOfLongestSubstring("abcabcbb")
#print s.lengthOfLongestSubstring("bbbbbbbbbb")

                
