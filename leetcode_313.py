class Solution:
    def getHash(self, cnt):
        h = 0
        for c in cnt:
          h = h * 31 + c
        return h

    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        result = []
        hashMap = {}
        for s in strs:
          cnt = [0 for x in range(26)]
          for c in s:
            cnt[ord(c) - ord('a')] += 1
          hashVal = self.getHash(cnt)
          if hashVal not in hashMap:
            hashMap[hashVal] = []
          hashMap[hashVal].append(s)
        for v in hashMap.values():
          if len(v) > 1:
            result.extend(v)

        return result
