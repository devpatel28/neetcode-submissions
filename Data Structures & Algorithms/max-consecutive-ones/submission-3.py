class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcons = max_loop = 0
        for i in nums:
            if i == 0:
                maxcons = max(maxcons, max_loop)
                max_loop = 0
            else:
                max_loop += 1

        return max(max_loop, maxcons)
                    