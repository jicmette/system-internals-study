def reverse_string(s: list):
    """
    Reverses a list of characters in-place using Two Pointers.
    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        # Move pointers inward
        left += 1
        right -= 1

    return s

# Test
my_str = ["h", "e", "l", "l", "o"]
print(f"Before: {my_str}")
reverse_string(my_str)
print(f"After:  {my_str}")