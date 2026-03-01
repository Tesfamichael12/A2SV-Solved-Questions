// Problem: Find Three Consecutive Integers That Sum to a Given Number
// Difficulty: Medium
// URL: https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
// Language: Python3
// Submitted: 2025-01-30T08:46:26.000Z
// Pushed via A2SV Companion

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        first = num // 3
        print(first)
        if first + first - 1 + first + 1 == num:
            return [first - 1,first, first + 1]
        else:
            return []