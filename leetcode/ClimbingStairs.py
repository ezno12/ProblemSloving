# 70. Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        pre, curr = 1, 2

        for _ in range(3, n + 1):
            curr, pre = curr + pre, curr

        return curr
