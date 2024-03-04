class Solution:
    def findMin(self, nums: List[int]) -> int:
        curMaxIdx, curMax = -1, float('-inf')
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[r]:
                return nums[l]
            elif nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid
        return l

        