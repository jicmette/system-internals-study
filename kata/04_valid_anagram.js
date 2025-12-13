/**
 * Checks if two strings are anagrams using a Frequency Counter.
 * Time: O(n)
 * Space: O(1) (Technically O(26) because mostly lowercase letters)
 */
function isAnagram(s, t) {
    if (s.length !== t.length) return false;

    const count = {};

    // Count letters in first string
    for (const char of s) {
        count[char] = (count[char] || 0) + 1;
    }

    // Subtract letters from second string
    for (const char of t) {
        if (!count[char]) {
            return false; // Letter doesn't exist or is zero
        }
        count[char]--;
    }


    return true;
}

// Test
console.log("Is Anagram:", isAnagram("anagram", "nagaram")); // true
console.log("Is Anagram:", isAnagram("rat", "car")); // false