class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, s, dic):
        result = []
        dic_len = len(dic)
        if dic_len == 0:
            return result
        word_len = len(dic[0])
        s_len = len(s)
        cat_len = len(dic) * word_len
        if word_len == 0 or s_len < word_len:
            return result

        for start in xrange(0, s_len - cat_len + 1):
            word_count = {}
            for word in dic:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            for i in xrange(start, start + cat_len, word_len):
                tmp_word = s[i:i + word_len]
                if tmp_word in word_count and word_count[tmp_word] > 0:
                    word_count[tmp_word] -= 1
                    if word_count[tmp_word] == 0:
                        word_count.pop(tmp_word)
                else:
                    break
            if len(word_count) == 0:
                result.append(start)
        return result


s = Solution()
#print s.findSubstring("barfoothefoobarman", ["foo", "bar"])
print s.findSubstring("a", ["a"])