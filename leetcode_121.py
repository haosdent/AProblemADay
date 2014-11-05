class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        reach = 0
        i = 0
        while i <= reach and reach < len(A):
            reach = max(reach, i + A[i])
            i += 1
        return reach >= len(A) - 1


s = Solution()
print s.canJump([0])
