// We use a Set because lookups are O(1) instant.
function containsDuplicate(nums) {
    const seen = new Set();

    for (const num of nums) {
        if (seen.has(num)) { // Check first
            return true; // Found it!
        }
        seen.add(num); // Act second
    }
    return false;
}

// Test
console.log(containsDuplicate([1, 2, 3, 1])); // true
console.log(containsDuplicate([1, 2, 3, 4])); // false