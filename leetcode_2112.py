class Solution:
    # @return a string
    def getPermutation(self, n, k):
        s = ''
        used = [False for x in range(n)]
        factor = 1
        for i in range(1, n):
            factor *= i

        k = k - 1
        for i in range(n):
            index = k / factor
            k %= factor
            for j in range(n):
                if not used[j]:
                    if index == 0:
                        used[j] = True
                        s += str(j + 1)
                        break
                    else:
                        index -= 1

            if n - 1 - i != 0:
                factor /= n - 1 - i

        return s

s = Solution()
print s.getPermutation(2, 1)
