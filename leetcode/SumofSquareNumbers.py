# 633. Sum of Square Numbers
#
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = int(c**0.5)
        if i * i == c:
            return True
        else:
            j = 1
            while j <= i:
                if i * i + j * j == c:
                    return True
                elif i * i + j * j < c:
                    j += 1
                else:
                    i -= 1
        return False
