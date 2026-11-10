class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        maximum = max(freq.values())
        answer = 0

        for count in freq.values():
            if count == maximum:
                answer += count
        return answer

        