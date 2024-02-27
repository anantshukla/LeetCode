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
            rear = nums[rear]
            if rear2 == rear:
                return rear2
            
            