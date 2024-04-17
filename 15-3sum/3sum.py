class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, num in enumerate(nums):
            if num > 0:
                break
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            l = idx + 1
            r = len(nums) - 1

            while l < r:
                currSum = nums[idx] + nums[l] + nums[r]

                if currSum == 0:
                    res.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            
                elif currSum > 0:
                    r -= 1
                else:
                    l += 1
        return res