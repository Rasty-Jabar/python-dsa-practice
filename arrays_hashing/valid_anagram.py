"""
Problem: Valid Anagram
Category: Arrays & Hashing
Difficulty: Easy

Explanation:
Two strings are anagrams if they contain the same characters with the same
frequencies. The order doesn't matter.

There are different ways to solve this, but the dictionary (hash map) approach
is very clear and works well:

- If the lengths differ, they cannot be anagrams.
- Count the frequency of each character in the first string.
- Subtract the frequency for each character in the second string.
- If all counts end at zero, the strings are anagrams.

This approach avoids sorting and keeps the logic simple to follow.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_anagram(s: str, t: str) -> bool:
    # Quick length check
    if len(s) != len(t):
        return False

    count = {}

    # Count characters in first string
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    # Subtract counts using second string
    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    # If all counts returned to zero, it's an anagram
    return True
