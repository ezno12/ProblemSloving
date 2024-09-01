# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        state = {}
        start, maxFruits = 0, 0

        for i in range(len(fruits)):
            state[fruits[i]] = state.get(fruits[i], 0) + 1

            while len(state) > 2:
                state[fruits[start]] -= 1
                if state[fruits[start]] == 0:
                    del state[fruits[start]]
                start += 1

            maxFruits = max(maxFruits, i - start + 1)

        return maxFruits
