# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        current_max = 0

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            current_area = width * min_height

            current_max = max(current_max, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return current_max
