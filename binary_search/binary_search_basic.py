"""
Problem: Binary Search (Basic)
Category: Binary Search
Difficulty: Easy

Explanation:
Binary search is a classic technique used on sorted arrays. The idea is to keep
halving the search space until the target is found:

- Start with two pointers: left and right.
- Find the middle index.
- If the middle value matches the target, return the index.
- If the target is smaller, move the right pointer left.
- If the target is larger, move the left pointer right.
- Repeat until the pointers cross.

This gives a very efficient O(log n) search time, which is a huge improvement
over scanning the whole list.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    # If not found
    return -1
