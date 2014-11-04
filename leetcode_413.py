class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)
        stack = []
        result = 0
        i = 0
        while i < len(height):
            if len(stack) == 0 or height[i] > height[stack[len(stack) - 1]]:
                stack.append(i)
                i += 1
            else:
                tmp = stack.pop()
                if len(stack) == 0:
                    result = max(result, i * height[tmp])
                else:
                    result = max(result, (i - stack[len(stack) - 1] - 1) * height[tmp])

        return result


s = Solution()
print s.largestRectangleArea([2, 1, 5, 6, 5, 3])
