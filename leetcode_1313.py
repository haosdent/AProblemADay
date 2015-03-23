class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dic):
        f = [False for x in xrange(len(s) + 1)]
        f[0] = True
        prev_map = {}
        for i in xrange(len(s) + 1):
            for j in xrange(i):
                if f[j] and s[j:i] in dic:
                    f[i] = True
                    if i not in prev_map:
                        prev_map[i] = []
                    prev_map[i].append(j)
        result = []
        self.findPath([len(s)], prev_map, s, result)
        return result

    def findPath(self, path, prev_map, s, result):
        path_last = path[len(path) - 1]
        if path_last == 0:
            tmp_pos = 0
            tmp_sen = ''
            for i in reversed(path):
                if i == 0:
                    continue
                tmp_sen += s[tmp_pos:i]
                tmp_sen += ' '
                tmp_pos = i
            if tmp_sen[len(tmp_sen) - 1] == ' ':
                tmp_sen = tmp_sen[:len(tmp_sen) - 1]
            result.append(tmp_sen)
        elif path_last in prev_map:
            prev = prev_map[path_last]
            for i in prev:
                path.append(i)
                self.findPath(path, prev_map, s, result)
                path.pop()


s = Solution()
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])