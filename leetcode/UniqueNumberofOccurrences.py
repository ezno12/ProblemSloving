# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        record = {}
        for num in arr:
            record[num] = record.get(num, 0) + 1

        values = list(record.values())
        print(values)
        uniqueValues = set(values)

        return len(values) == len(uniqueValues)
