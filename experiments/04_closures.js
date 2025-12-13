// 04_closures.js
// Experiment: Closures & Lexical Scope
// Goal: Create "Private State" using only functions (The Module Pattern).

console.log("--- EXPERIMENT START ---");

function createCounter() {
    // 1. The Private Variable
    // This lives inside the function's scope.
    // Normally, when the function ends, this variable is destroyed.
    let count = 0;

    // 2. The Return Value (The Interface)
    // We return an object containing TWO functions.
    // These functions act as a "Backdoor" to access 'count'.
    return {
        increment: function() {
            count++;
            console.log(`Count incremented to: ${count}`);
        },
        getCount: function() {
            return count;
        }
    };
}

// 3. The Setup
// I run the function ONCE. It finishes running.
// Logic says 'count' should be gone.
const myCounter = createCounter();

console.log("Initial Check:", myCounter.getCount()); // 0

// 4. The Action
console.log("\n[Using the Public Interface]");
myCounter.increment(); // 1
myCounter.increment(); // 2
myCounter.increment(); // 3

console.log("Current Count:", myCounter.getCount()); // 3

// 5. The Hack Attempt
console.log("\n[Attempting to Hack...]");
myCounter.count = 999; // Trying to overwrite it directly
console.log("Did hack work? Value is:", myCounter.getCount());
// Expected: 3 (Hack failed!)

console.log("\nCONCLUSION: 'count' is alive in the Closure, protecting it from direct access.");
console.log("--- EXPERIMENT END ---");