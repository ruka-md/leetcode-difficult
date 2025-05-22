# 0004. Median of Two Sorted Arrays

## Difficulty
**Hard**

## Problem
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be **O(log (m+n))**.

[LeetCode Link](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Examples

**Input:**  
nums1 = [1, 2], nums2 = [3, 4]  
**Output:**  
2.5

**Input:**  
nums1 = [1, 3], nums2 = [2]  
**Output:**  
2.0

## Approach

We perform binary search on the **shorter array** to find a partition that divides both arrays into two halves such that:

- All elements in the left halves ≤ all elements in the right halves.
- The left half contains `(m + n + 1) // 2` elements, so that we can easily pick the median from the boundaries.

At each step:

- `i` = partition index in `nums1`
- `j` = partition index in `nums2` = `(m + n + 1) // 2 - i`

We use `float('-inf')` and `float('inf')` for edge cases where partitions go out of bounds.

Once a valid partition is found:
- If total length is odd → return `max(lefts)`
- If total length is even → return `(max(lefts) + min(rights)) / 2`

## Code
See [solution.py](./solution.py)

## Complexity
- Time: O(log(min(m, n)))
- Space: O(1)
