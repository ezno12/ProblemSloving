# LeetCode 933 - Number of Recent Calls

Pattern: Design + Queue (Sliding Window)

Difficulty: Easy

## Idea

Maintain a deque of request timestamps. Every time ping(t) is called, add t to the front of the deque.

Then repeatedly remove timestamps from the back of the deque that fall outside the trailing 3000ms window (older than t - 3000).

The size of the deque after cleanup is the number of requests within the last 3000ms.

## Complexity

* Time: O(1) amortized per call
* Space: O(n) for the deque of recent timestamps

## Mistakes

* Solved cleanly on the first accepted attempt. Using a deque lets both adding new timestamps and trimming old ones happen in O(1) amortized time, rather than scanning a growing list each call.

## Recognition

Look for this pattern when you have:

* A stream of events/timestamps where only a trailing time window matters
* Old entries outside the window need to be discarded incrementally
* A deque efficiently supports adding to one end and removing from the other

## Keywords

* Design
* Queue
* Data Stream
* Sliding Time Window

## Similar Problems

* 346. Moving Average from Data Stream
* 239. Sliding Window Maximum
* 1352. Product of the Last K Numbers