class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) > 0:
            result = A[0]
        else:
            result = 0
        f = []
        for i in range(len(A)):
            if i == 0 or f[i - 1] <= 0:
                f.append(A[i])
            else:
                f.append(f[i - 1] + A[i])
            result = max(result, f[i])

        return result

s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print s.maxSubArray([-1])
