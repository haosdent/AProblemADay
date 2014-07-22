class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if len(A) == 0:
            return
        x = 0
        for e in A:
            x ^= e
        return x

if __name__ == "__main__":
    s = Solution()
    print s.singleNumber([1, 2, 3, 5, 1, 2, 3])
