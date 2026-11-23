class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcons = max_loop = 0
        for i in nums:
            max_loop = max_loop + 1 if i else 0
            maxcons = max(maxcons, max_loop)

        return maxcons
                    