class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        rear, forward = 0, 0

        while True:
            rear = nums[rear]
            forward = nums[nums[forward]]
            if rear == forward:
                break
        
        rear = 0
        while True:
            rear = nums[rear]
            forward = nums[forward]
            if forward == rear:
                return forward
            
            