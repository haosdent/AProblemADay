class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index_map = {}
        num_len = len(num)
        for i in xrange(num_len):
            index_map[num[i]] = i
        for i in xrange(num_len):
            remain = target - num[i]
            if remain in index_map and index_map[remain] != i:
                return i + 1, index_map[remain] + 1


s = Solution()
print s.twoSum([2, 7, 11, 15], 9)