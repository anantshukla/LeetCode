class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res =[]
        for i, num in enumerate(nums):
            for j in self.permute(nums[:i] + nums[i+1:]):
                res.append([num] + j)
        return res