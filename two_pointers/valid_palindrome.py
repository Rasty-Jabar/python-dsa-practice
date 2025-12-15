"""
Problem: Valid Palindrome
Category: Two Pointers
Difficulty: Easy

Explanation:
A string is a palindrome if it reads the same forwards and backwards.
To solve this efficiently, I use the classic two-pointer technique:

- Clean the string first by keeping only alphanumeric characters
  and converting everything to lowercase.
- Set one pointer at the start and one at the end.
- Move both pointers inward while checking characters.
- If the characters differ at any point, it's not a palindrome.

This avoids creating a reversed copy of the whole string and keeps the solution
simple and memory efficient.

Time Complexity: O(n)
Space Complexity: O(1) after cleaning the string
"""

def is_palindrome(s: str) -> bool:
    # Keep only alphanumeric characters and lowercase them
    cleaned = [ch.lower() for ch in s if ch.isalnum()]

    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True
