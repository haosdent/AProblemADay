class Solution:
    # @return an integer
    def maxArea(self, height):
        start = 0
        end = len(height)
        result = 0
        while start < end:
            result = max(result, min(height[start], height[end - 1]) * (end - 1 - start))
            if height[start] < height[end - 1]:
                start += 1
            else:
                end -= 1
        return result


s = Solution()
print s.maxArea([1, 2, 3, 4, 5])
print s.maxArea([])
