class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        lefts = [0 for x in range(len(A))]
        rights = [0 for x in range(len(A))]
        n = len(A)
        for i in range(1, n):
            lefts[i] = max(lefts[i - 1], A[i - 1])
            rights[n - i - 1] = max(rights[n - i], A[n - i])

        s = 0
        for i in range(1, len(A) - 1):
            h = min(lefts[i], rights[i])
            if h > A[i]:
                s += h - A[i]


        return s

s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
