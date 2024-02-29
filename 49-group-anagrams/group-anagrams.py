class Solution:
    # TC: O(m * n), where m is the number of elements, n is the length of string
    # SC: O(m * 26)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = collections.defaultdict(list)
        for word in strs:
            charArr = [0] * 26
            for char in word:
                charArr[ord(char) - ord('a')] += 1
            # Tuple is immutable and therefore can be hashed
            hMap[tuple(charArr)].append(word)
        return hMap.values()