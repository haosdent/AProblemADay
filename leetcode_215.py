class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        total = len(A) + len(B)
        if total & 1:
            return self.findKth(A, 0, B, 0, total / 2 + 1)
        else:
            return (self.findKth(A, 0, B, 0, total / 2) + self.findKth(A, 0, B, 0, total / 2 + 1)) / 2.0
        
    def findKth(self, A, sa, B, sb, k):
        m = len(A) - sa
        n = len(B) - sb
        if m > n:
            return self.findKth(B, sb, A, sa, k)
        if m == 0:
            i = sb + k - 1
            return B[i]
        if k == 1:
            return min(A[sa], B[sb])

        pa = sa + min(k / 2, m)
        pb = sb + (k - (pa - sa))
        if A[pa - 1] < B[pb - 1]:
            return self.findKth(A, pa, B, sb, k - (pa - sa))
        elif A[pa - 1] > B[pb - 1]:
            return self.findKth(A, sa, B, pb, k - (pb - sb))
        else:
            return A[pa - 1]

s = Solution()
a = [1, 2, 3, 4]
b = [1, 5, 7]
print s.findMedianSortedArrays([], [2, 3])
