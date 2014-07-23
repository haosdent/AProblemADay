class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if len(A) == 0:
            return
        ones = 0
        twos = 0
        for e in A:
            ones = (~twos) & (ones ^ e)
            twos = (~ones) & (twos ^ e)
        return ones

