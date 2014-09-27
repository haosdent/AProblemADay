class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        cloest = 9223372036854775807
        if num is None or len(num) == 0:
            return cloest

        num.sort()
        if len(num) <= 2:
            return sum(num)
        for i in range(len(num) - 2):
            left = i + 1
            right = len(num) - 1
            while left < right:
                s = num[i] + num[left] + num[right]
                if s == target:
                    return target
                elif s < target:
                    left += 1
                else:
                    right -= 1
                if abs(target - s) < abs(target - cloest):
                    cloest = s

        return cloest


s = Solution()
print s.threeSumClosest([-1, 2, 1, -4], 1)
