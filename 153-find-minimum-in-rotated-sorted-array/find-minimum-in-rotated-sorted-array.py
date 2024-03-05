class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r) // 2
            minVal = min(minVal, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid
        return minVal
        