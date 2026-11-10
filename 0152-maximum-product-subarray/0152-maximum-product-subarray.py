class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maximum = minimum = answer = nums[0]

        for x in nums[1:]:
            if x < 0:
                minimum, maximum = maximum, minimum

            maximum = max(x, maximum * x)
            minimum = min(x, minimum * x)

            answer = max(answer, maximum)
        return answer

        