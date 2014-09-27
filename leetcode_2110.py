class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        index = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[index] = A[i]
                index += 1
        print A
        return index
        
s = Solution()
print s.removeElement([1, 2, 3, 4], 2)
