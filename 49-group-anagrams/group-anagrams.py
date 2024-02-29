class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = collections.defaultdict(list)
        for word in strs:
            charArr = [0] * 26
            for char in word:
                charArr[ord(char) - ord('a')] += 1
            # charStr = ''.join(map(str, charArr))
            hMap[tuple(charArr)].append(word)
        return hMap.values()