from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = half - i

            short_left  = nums1[i - 1] if i > 0 else float('-inf')
            short_right = nums1[i]     if i < m else float('inf')
            long_left   = nums2[j - 1] if j > 0 else float('-inf')
            long_right  = nums2[j]     if j < n else float('inf')

            if short_left <= long_right and long_left <= short_right:
                if (m + n) % 2 == 0:
                    return (max(short_left, long_left) + min(short_right, long_right)) / 2
                else:
                    return max(short_left, long_left)
            elif short_left > long_right:
                right = i - 1
            else:
                left = i + 1
