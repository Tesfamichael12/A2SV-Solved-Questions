// Problem: Container With Most Water
// Difficulty: Medium
// URL: https://leetcode.com/problems/container-with-most-water/
// Language: Python3
// Submitted: 2025-02-12T13:38:32.000Z
// Pushed via A2SV Hub

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) -1 
        while l <= r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else:
                l += 1
        
        return max_area