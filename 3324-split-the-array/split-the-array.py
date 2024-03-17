class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        for val in hashMap.values():
            if val > 2:
                return False
        return True
        