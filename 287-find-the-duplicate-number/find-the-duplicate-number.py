class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        rear, forward = 0, 0

        while True:
            rear = nums[rear]
            forward = nums[nums[forward]]
            if rear == forward:
                break
        
        rear2 = 0
        while True:
            rear2 = nums[rear2]
            forward = nums[forward]
            if rear2 == forward:
                return rear2
            
            