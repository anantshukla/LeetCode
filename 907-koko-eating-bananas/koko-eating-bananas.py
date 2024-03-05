class Solution:
    # O(n * log m)
    # Reducing the search space by applying binary sort over speed 1 - max(piles)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minSpeed = right

        while left <= right:
            mid = (left + right) // 2
            
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
                        
            if time <= h:
                # Success. Go left - Speed can be reduced-> minimizing
                minSpeed = mid
                right = mid - 1
            else:
                # Go right - Speed needs to be increased
                left = mid + 1
                
        return minSpeed

    
    # # Time Complexity - O(m * n) where m = max(piles)
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     # Starting from number of len(piles) towards max(piles), we will converge at k
    #     n = len(piles)
    #     maxHeight = max(piles)
    #     rateOfEating = 1
    #     while True:
    #         currHours = 0
    #         for pile in piles:
    #             currHours += math.floor(pile / rateOfEating)

    #         if currHours <= h:
    #             return rateOfEating
    #         rateOfEating +=1
        
        