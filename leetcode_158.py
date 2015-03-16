class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        if numRows <= 0:
            return []
        tmp_row = [1]
        result.append([1])
        for i in xrange(1, numRows):
            tmp_row.insert(0, 0)
            tmp_row.append(0)
            now_row = []
            for j in xrange(len(tmp_row) - 1):
                now_row.append(tmp_row[j] + tmp_row[j + 1])
            tmp_row = now_row
            copy_row = []
            for e in now_row:
                copy_row.append(e)
            result.append(copy_row)
        return result


s = Solution()
print s.generate(5)