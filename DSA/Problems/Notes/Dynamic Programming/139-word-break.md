# LeetCode 139 - Word Break

Pattern: Dynamic Programming (Top-Down Memoization)

Difficulty: Medium

## Idea

Use recursion with memoization: dfs(start_index) is true if the substring from start_index to the end can be fully segmented into dictionary words.

At each index, try every word in wordDict; if the substring starting there begins with that word, recurse on the remainder (start_index + len(word)).

## Complexity

* Time: O(n * m * k) where n is string length, m is dictionary size, k is average word length (as implemented, without a length-bounded optimization)
* Space: O(n) for memoization

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from an early version that did not memoize correctly, causing either wrong results on overlapping subproblems or a timeout on longer strings.

## Recognition

Look for this pattern when you have:

* A string that must be segmented into valid dictionary words
* Overlapping subproblems (many starting indices get revisited), which memoization resolves
* A boolean feasibility question rather than counting all ways (see Word Break II for that variant)

## Keywords

* Dynamic Programming
* Memoization
* String Segmentation
* Trie (alternative optimization)

## Similar Problems

* 140. Word Break II
* 91. Decode Ways
* 322. Coin Change