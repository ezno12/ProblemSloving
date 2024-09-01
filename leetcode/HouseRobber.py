# 198. House Robber
# https://leetcode.com/problems/house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now
