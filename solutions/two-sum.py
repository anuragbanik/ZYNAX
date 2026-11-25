# LeetCode 1: Two Sum
# Student: Anurag Banik (Roll: 2026ABES042)
# ABES EC - CSE (AI/ML)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map: O(N) Time, O(N) Space
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []

if __name__ == '__main__':
    s = Solution()
    print('Two Sum Test:', s.twoSum([2, 7, 11, 15], 9)) # Expected: [0, 1]
