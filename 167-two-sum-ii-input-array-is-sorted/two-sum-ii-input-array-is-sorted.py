class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr, r_ptr = 0, len(numbers) - 1

        while l_ptr < r_ptr:
            sum = numbers[l_ptr] + numbers[r_ptr]
            if sum == target:
                break
            elif sum > target:
                r_ptr -= 1
            else:
                l_ptr += 1
        
        return [l_ptr + 1, r_ptr + 1]