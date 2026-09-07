# LeetCode 133 - Clone Graph

Pattern: Graph Theory + Breadth-First Search

Difficulty: Medium

## Idea

Use a hash map (copies) to track the mapping from original nodes to their cloned counterparts, so each node is only cloned once even if visited multiple times through different edges.

Do a BFS starting from the given node: for every node popped from the queue, go through its neighbors, cloning any neighbor not already in the map and adding it to the queue, then attach the cloned neighbor to the current clone's neighbor list.

## Complexity

* Time: O(V + E)
* Space: O(V) for the hash map and queue

## Mistakes

* Solved cleanly on the first accepted attempt. The key trick is cloning a node's shallow copy (with an empty neighbor list) as soon as it is first encountered and BEFORE fully cloning its neighbors, which correctly handles cycles in the graph.

## Recognition

Look for this pattern when you have:

* A graph (possibly with cycles) that must be deep-copied
* A hash map from original node to cloned node prevents infinite loops and duplicate cloning

## Keywords

* Graph Theory
* Breadth-First Search
* Depth-First Search (alternative)
* Hash Table
* Deep Copy

## Similar Problems

* 138. Copy List with Random Pointer
* 130. Surrounded Regions
* 200. Number of Islands