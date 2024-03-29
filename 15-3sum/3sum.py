class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        

        for i in range(len(nums)):
            # Can skip the postive i - numbers
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sumV = nums[i] + nums[j] + nums[k]

                if sumV == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                       j += 1
                     
                elif sumV > 0:
                    k -= 1
                else:
                    j += 1
        
        return output