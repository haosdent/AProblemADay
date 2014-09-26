class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n <= 1:
            return n

        index = 1;
        for i in range(1, n):
            if A[index - 1] != A[i]:
                A[index] = A[i]
                index += 1

        return index


s = Solution()
a = [1, 1, 1, 2, 3]
print s.removeDuplicates(a)
