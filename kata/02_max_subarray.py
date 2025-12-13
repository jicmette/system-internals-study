def max_sub_array(nums: list) -> int:
    """
    Finds the maximum sum of a contiguous subarray.
    Pattern: Kadane's Algorithm / Dynamic Programming
    Time: O(n)
    Space: O(1)
    """
    current_sum = 0
    max_sum = float('-inf') # "Sentinel Value" Start with the smallest possible number

    for num in nums:
        # Logic: Should I start a new subarray with just 'num',
        # or extend the existing 'current_sum'?
        if current_sum < 0:
            current_sum = num  # Reset: The past was dragging it down.
        else:
            current_sum += num # Keep going: The past is positive.

        # Did it beat the record?
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

# Test
data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Result: {max_sub_array(data)}") # Should be 6 (from [4, -1, 2, 1])