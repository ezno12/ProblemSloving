# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        state, start, minLen = 0,0, float('inf') 

        for end in range(len(nums)):
            state += nums[end]

            while state >= target:
                state -= nums[start]
                minLen = min(minLen, end - start + 1)
                start += 1
        return 0 if minLen == float('inf') else minLen 
