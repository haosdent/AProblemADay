class Solution:
    def getRow(self, rowIndex):
        if rowIndex <= 0:
            return [1]
        result_row = [1]
        for i in xrange(1, rowIndex + 1):
            result_row.insert(0, 0)
            result_row.append(0)
            now_row = []
            for j in xrange(len(result_row) - 1):
                now_row.append(result_row[j] + result_row[j + 1])
            result_row = now_row
        return result_row


s = Solution()
print s.getRow(3)