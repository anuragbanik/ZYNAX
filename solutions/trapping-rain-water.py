# LeetCode 42: Trapping Rain Water
# Student: Anurag Banik (Roll: 2026ABES042)
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water

if __name__ == '__main__':
    s = Solution()
    print('Trap Water Test:', s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # Expected: 6
