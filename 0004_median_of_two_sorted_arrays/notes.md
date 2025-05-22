# Notes

- 🔍 **Binary search is always performed on the shorter array.**
  - This guarantees logarithmic time complexity and prevents index overflow issues.

- 🧮 **We only binary search in the shorter array**, and calculate the corresponding partition index in the longer array to keep the left side containing exactly `(m + n + 1) // 2` elements.

- ♻️ **We ensure nums1 is the shorter array by swapping if necessary:**
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

- 📐 **`left` and `right` refer to "gaps" between elements**, not element indices.
  - This means we are partitioning between values, not on them directly.
  - For an array of length `m`, the binary search runs from `left = 0` to `right = m`.

- 🧱 **Edge values are safely handled using `float('-inf')` and `float('inf')`.**
  - This makes partition boundary conditions (like empty left or right sides) clean and robust.
