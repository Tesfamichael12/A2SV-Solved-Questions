// Problem: Convert the Temperature
// Difficulty: Easy
// URL: https://leetcode.com/problems/convert-the-temperature/
// Language: Python3
// Submitted: 2026-03-01T09:10:01.000Z
// Pushed via A2SV Hub

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius*1.80 + 32.00]