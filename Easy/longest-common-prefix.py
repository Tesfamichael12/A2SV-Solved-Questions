// Problem: Longest Common Prefix
// Difficulty: Easy
// URL: https://leetcode.com/problems/longest-common-prefix/
// Language: Python3
// Submitted: 2026-02-27T14:20:42.000Z
// Pushed via A2SV Hub

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        largest = strs[0]
        smallest = strs[0]

        for c in strs:
            if largest < c:
                largest = c
            if smallest > c:
                smallest = c
        
        i = 0
        while i < len(smallest):
            if largest[i] == smallest[i]:
                i += 1
            else: break
        
        return smallest[:i]
