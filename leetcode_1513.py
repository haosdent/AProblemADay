class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = 1
        if dividend > 0 and divisor < 0:
            sign = -1
        elif dividend < 0 and divisor > 0:
            sign = -1
        if dividend < 0:
            a = -dividend
        else:
            a = dividend
        if divisor < 0:
            b = -divisor
        elif divisor == 0:
            return 0
        else:
            b = divisor

        result = 0
        while a >= b:
            c = b
            i = 0
            while a - c >= 0:
                a -= c
                c = c * 2
                result += 1 << i
                i += 1

        if result > 2147483647 and sign == 1:
            result = 2147483647
        elif result > 2147483648 and sign == -1:
            result = 2147483648

        return result * sign


s = Solution()
print s.divide(4, 2)
