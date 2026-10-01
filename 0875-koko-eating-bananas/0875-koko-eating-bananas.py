import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The minimum possible eating speed is 1 banana per hour.
        # The maximum useful speed is the size of the largest pile.
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            # Calculate the total hours needed to finish all piles at 'mid' speed
            # math.ceil(p / mid) gives the hours needed for a single pile
            total_hours = sum(math.ceil(p / mid) for p in piles)
            
            # If Koko can finish within h hours, this speed is valid.
            # We try to find a smaller valid speed by moving the right pointer.
            if total_hours <= h:
                right = mid
            else:
                # If it takes too long, we must increase the speed.
                left = mid + 1
                
        return left
