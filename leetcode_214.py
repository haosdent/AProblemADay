class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        first = 0
        last = len(A)
        while (first != last):
            mid = (first + last) / 2
            if A[mid] == target:
                return True
            if A[first] < A[mid]:
                if A[first] <= target and target <= A[mid]:
                    last = mid
                else:
                    first = mid + 1
            elif A[first] > A[mid]:
                if A[mid] <= target and target <= A[last - 1]:
                    first = mid + 1
                else:
                    last = mid
            else:
                first += 1

        return False


s = Solution()
a = [3, 1]
print s.search(a, 2)
