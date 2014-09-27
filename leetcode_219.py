import collections

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums = sorted(nums)
        result = set()
        cache  = collections.defaultdict(set)
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for half in cache[target - nums[i] - nums[j]]:
                    result.add(tuple(list(half) + [nums[i], nums[j]]))

            for j in range(i):
                cache[nums[i] + nums[j]].add((nums[j], nums[i]))

        return map(list, result)

s = Solution()
s.fourSum([1, 0, -1, 0, -2, 2], 0)
