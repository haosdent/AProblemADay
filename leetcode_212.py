class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n <= 2:
            return n

        index = 2;
        for i in range(2, n):
            if A[index - 2] != A[i]:
                A[index] = A[i]
                index += 1

        return index


s = Solution()
a = [1, 1, 1, 2, 3]
print s.removeDuplicates(a)
