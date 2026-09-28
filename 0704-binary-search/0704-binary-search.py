from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Calculate the middle index (using floor division)
            mid = (left + right) // 2
            
            # Check if target is present at mid
            if nums[mid] == target:
                return mid
            # If target is smaller, ignore right half
            elif nums[mid] > target:
                right = mid - 1
            # If target is larger, ignore left half
            else:
                left = mid + 1
                
        # Target was not found in the array
        return -1
