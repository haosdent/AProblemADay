class Solution:
    def intToRoman(self, num):
	m = ['', 'M', 'MM', 'MMM']
	c = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
	x = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
	i = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']	
	result = m[num / 1000] + c[num % 1000 / 100] + x[num % 100 / 10] + i[num % 10]
	return result

s = Solution()
print s.intToRoman(1)
