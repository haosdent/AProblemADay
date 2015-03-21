class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, l):
        result = []
        words_len = len(words)
        begin = 0
        sen_len = 0
        for i in xrange(words_len):
            if sen_len + len(words[i]) + i - begin > l:
                result.append(self.addSpaces(words, begin, i - 1, sen_len, l))
                begin = i
                sen_len = len(words[i])
            else:
                sen_len += len(words[i])
        if begin <= words_len - 1:
            sen = ' '.join(words[begin:])
            result.append(sen + ' ' * (l - len(sen)))
        return result

    def addSpaces(self, words, begin, end, sen_len, l):
        range_len = end + 1 - begin
        if range_len <= 1:
            return words[begin] + ' ' * (l - len(words[begin]))

        space_cnt = (l - sen_len) / (range_len - 1)
        ext_space_len = (l - sen_len) % (range_len - 1)
        sen = ''
        for i in xrange(ext_space_len):
            sen += words[begin + i] + (space_cnt + 1) * ' '
        for i in xrange(ext_space_len, end - begin):
            sen += words[begin + i] + space_cnt * ' '
        sen += words[end]
        return sen


s = Solution()
#print s.fullJustify(["a","b","c","d","e"], 3)
print s.fullJustify(["Listen","to","many,","speak","to","a","few."], 6)
#print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
#print s.fullJustify(["a","b","c","d","e"], 1)
