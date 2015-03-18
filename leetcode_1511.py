class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for x in xrange(n)] for y in xrange(n)]
        beginX = 0
        beginY = 0
        endY = len(matrix) - 1
        if endY < 0:
            return matrix
        endX = len(matrix[0]) - 1
        num = 0
        while True:
            for i in xrange(beginX, endX + 1):
                num += 1
                matrix[beginY][i] = num
            beginY += 1
            if beginY > endY:
                break
            for i in xrange(beginY, endY + 1):
                num += 1
                matrix[i][endX] = num
            endX -= 1
            if beginX > endX:
                break
            for i in xrange(endX, beginX - 1, -1):
                num += 1
                matrix[endY][i] = num
            endY -= 1
            if beginY > endY:
                break
            for i in xrange(endY, beginY - 1, -1):
                num += 1
                matrix[i][beginX] = num
            beginX += 1
            if beginX > endX:
                break
        return matrix


s = Solution()
print s.generateMatrix(3)