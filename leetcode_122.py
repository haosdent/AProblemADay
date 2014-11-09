class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        last = 0
        cur = 0
        result = 0
        i = 0
        while i < len(A) - 1 and i <= cur:
            cur = max(cur, i + A[i])
            if i == last:
                result += 1
                last = cur
            i += 1
        if last < len(A) - 1:
            result = 0
        return result


s = Solution()
print s.jump([2,3,1,1,4])
print s.jump([2,1])
