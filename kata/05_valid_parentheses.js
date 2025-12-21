function isValid(s) {
    // The Stack: LIFO (Last In, First Out)
    const stack = [];
    const map = {
        '(': ')',
        '{': '}',
        '[': ']'
    };

    for (const char of s) {
        // If it's an OPEN bracket (a key in our map)
        if (map[char]) {
            stack.push(map[char]); // Push the EXPECTED closing bracket
        } else {
            // It's a CLOSE bracket.
            // Pop the last expected bracket and compare.
            if (stack.pop() !== char) {
                return false;
            }
        }
    }
    // Valid only if stack is empty (no unclosed brackets left)
    return stack.length === 0;
}

// Test
console.log("()[]{}", isValid("()[]{}")); // true
console.log("(]", isValid("(]"));         // false