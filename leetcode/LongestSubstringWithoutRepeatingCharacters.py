# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        start = 0
        maxSub = 0

        for end in range(len(s)):

            if s[end] in charMap:
                start = max(start, charMap[s[end]] + 1)
            charMap[s[end]] = end

            maxSub = max(maxSub, end - start + 1)

        return maxSub
