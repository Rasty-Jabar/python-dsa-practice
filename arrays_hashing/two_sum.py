"""
Problem: Two Sum
Category: Arrays & Hashing
Difficulty: Easy

Explanation:
I solve this using a dictionary because it lets me check whether I have already
seen the complementary value (target - current number) in constant time.

The idea is simple:
- Loop through the array once.
- For each number, compute the value needed to reach the target.
- If I've already seen that needed value, I can immediately return both indices.
- Otherwise, store the current number's index in the dictionary.

This avoids a nested loop and gives an O(n) time solution,
which is much better than the basic O(n^2) brute force approach.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    seen = {}  

    for i, value in enumerate(nums):
        needed = target - value

        # If the number we need is already seen, return the pair
        if needed in seen:
            return [seen[needed], i]

        # Otherwise store the current number with its index
        seen[value] = i

    # If no solution exists (not expected in the Two Sum problem definition)
    return None
