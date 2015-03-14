class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        d = 1
        while x / d >= 10:
            d *= 10
        while x > 0:
            h = x / d
            t = x % 10
            print h, t
            if h != t:
                return False
            x = x % d / 10
            d /= 100

        return True


s = Solution()
print s.isPalindrome(121)
print s.isPalindrome(1000021)