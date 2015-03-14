class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        d = 1
        while x / d >= 10:
            d *= 10
        while x >= 10:
            h = x / d
            t = x % 10
            if h != t:
                return False
            x = x % d / 10
            d /= 10

        return True


s = Solution()
print s.isPalindrome(0)
print s.isPalindrome(1234)
print s.isPalindrome(10111)
