# LeetCode 752 - Open the Lock

Pattern: Breadth-First Search (Shortest Path on Implicit Graph)

Difficulty: Medium

## Idea

Treat every possible 4-digit combination as a node in an implicit graph, where each move (turning one wheel up or down) is an edge to a neighboring combination.

Do a BFS starting from "0000", skipping any combination in deadends, and tracking visited combinations to avoid repeats.

The first time the target combination is reached, the current BFS depth (steps) is the answer, since BFS explores in increasing order of move count.

## Complexity

* Time: O(10^4 * 8) since each of the 10000 combinations has 8 possible neighbor moves
* Space: O(10^4) for the visited set

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from not marking "0000" as visited before starting, or from forgetting to check "0000" against deadends at the very start.

## Recognition

Look for this pattern when you have:

* A state-space search where each state has a fixed number of possible transitions
* Need the MINIMUM number of moves/steps, which BFS guarantees (unlike DFS)

## Keywords

* Breadth-First Search
* Shortest Path
* Implicit Graph
* State Space Search
* Bidirectional Search (optimization)

## Similar Problems

* 433. Minimum Genetic Mutation
* 127. Word Ladder
* 815. Bus Routes