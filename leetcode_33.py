class Solution:
    # @return an integer
    def atoi(self, s):
        int_max = 2147483647
        int_min = 2147483648
        s_len = len(s)
        num = 0
        sign = 1
        if s_len == 0:
            return 0
        for i in range(s_len):
            if s[i] != ' ':
                break
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        for j in range(i, s_len):
            if s[j] < '0' or s[j] > '9':
                break
            tmp = int(s[j])
            if sign > 0:
                if num > int_max / 10 or int_max - num * 10 <= tmp:
                    return int_max
            else:
                if num > int_min / 10 or int_min - num * 10 <= tmp:
                    return int_min * sign                
            num = num * 10 + tmp

        return num * sign


s = Solution()
print s.atoi('   +123as23')
print s.atoi('')
