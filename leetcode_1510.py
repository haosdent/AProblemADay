class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        beginX = 0
        beginY = 0
        endY = len(matrix) - 1
        if endY < 0:
            return result
        endX = len(matrix[0]) - 1
        while True:
            for i in xrange(beginX, endX + 1):
                result.append(matrix[beginY][i])
            beginY += 1
            if beginY > endY:
                break
            for i in xrange(beginY, endY + 1):
                result.append(matrix[i][endX])
            endX -= 1
            if beginX > endX:
                break
            for i in xrange(endX, beginX - 1, -1):
                result.append(matrix[endY][i])
            endY -= 1
            if beginY > endY:
                break
            for i in xrange(endY, beginY - 1, -1):
                result.append(matrix[i][beginX])
            beginX += 1
            if beginX > endX:
                break
        return result

s = Solution()
print s.spiralOrder([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]])
print s.spiralOrder([[ 1 ]])