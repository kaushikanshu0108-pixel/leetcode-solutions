class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)

        if n == 0:
            return 
        k %= n
        nums[:] = nums[-k:] + nums[:-k] if k else nums[:]
