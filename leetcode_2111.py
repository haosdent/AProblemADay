class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        for i in range(len(num) - 2, -1, -1):
            if num[i + 1] > num[i]:
                j = 0
                for j in range(len(num) - 1, i, -1):
                    if num[j] > num[i]:
                        break

                num[i], num[j] = num[j], num[i]
                self.reverse(num, i + 1, len(num) - 1)
                return num
        return self.reverse(num, 0, len(num) - 1)

    def reverse(self, num, i, j):
        while i < j:
            num[i], num[j] = num[j], num[i]
            i += 1
            j -= 1
        return num


s = Solution()
a = [4,3,2,1]
a = [1]
s.nextPermutation(a)
print a
