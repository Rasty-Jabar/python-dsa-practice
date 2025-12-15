"""
Problem: Longest Substring Without Repeating Characters
Category: Sliding Window
Difficulty: Medium

Explanation:
The goal is to find the length of the longest substring where all characters are
unique. A classic way to solve this is with the sliding window technique:

- Use two pointers (left and right) to represent a window in the string.
- Expand the window by moving the right pointer.
- Keep a set of characters currently inside the window.
- If the new character is already in the set, shrink the window from the left
  until the duplicate is removed.
- Track the maximum window size along the way.

This avoids restarting the search after every duplicate and gives us an O(n)
solution, which is much more efficient than the naive O(n^2) approach.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # If we hit a duplicate, shrink the window from the left
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # Add the current character and update max length
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
