"""
Problem: Search in Rotated Sorted Array
Category: Binary Search
Difficulty: Medium

Explanation:
The array is originally sorted, but then rotated at some pivot.
For example: [4,5,6,7,0,1,2]

The key idea is that even after rotation, at least one half of the array
(left or right) is still sorted. We can use this to decide which side to discard
during each step of binary search:

- Check which half is sorted.
- If the target lies inside the sorted half, move the search boundaries into it.
- Otherwise, search the other half.

This keeps the overall time complexity at O(log n), similar to normal binary search,
just with some extra logic.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Found the target
        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # If target lies in this sorted half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Otherwise the right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    # Target not found
    return -1
