class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            num, diff = nums[i], target - nums[i]
            if diff in hm:
                return [hm[diff], i]
            else:
                hm[num] = i