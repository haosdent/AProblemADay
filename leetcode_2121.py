class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        inc = 1
        incs = []
        for i in ratings:
            incs.append(1)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                inc += 1
                incs[i] = max(inc, incs[i])
            else:
                inc = 1

        inc = 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                inc += 1
                incs[i] = max(inc, incs[i])
            else:
                inc = 1

        return sum(incs)

if __name__ == "__main__":
    s = Solution()
    print s.candy([2, 1])
