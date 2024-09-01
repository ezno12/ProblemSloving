# 881. Boats to Save People
#
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boatCount, left, right = 0, 0, len(people) - 1
        while right >= left:
            totalWeight = people[left] + people[right]

            if totalWeight <= limit:
                left += 1

            right -= 1
            boatCount += 1

        return boatCount
