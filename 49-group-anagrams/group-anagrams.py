class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for word in strs:
            freqCount = [0] * 26
            for c in word:
                freqCount[ord(c) - ord('a')] += 1
            hashMap[tuple(freqCount)].append(word)
        return hashMap.values()
