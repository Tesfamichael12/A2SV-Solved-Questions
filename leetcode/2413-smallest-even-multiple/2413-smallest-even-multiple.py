// Problem: Smallest Even Multiple
// Difficulty: Easy
// URL: https://leetcode.com/problems/smallest-even-multiple/
// Language: Python3
// Submitted: 2026-03-01T08:05:13.000Z
// Pushed via A2SV Hub

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return 2*n

        # updated