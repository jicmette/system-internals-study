// 03_js_references.js
// Experiment: Const vs Mutability
// Goal: Show that const prevents REASSIGNMENT, but not MUTATION.

console.log("--- EXPERIMENT START ---");

// PART 1: The Primitive (Immutable)
// Numbers are "passed by value". I can't change 100 into 200.
// I can only change what 'score' points to.
let score = 100;
let highScore = score; // Copies the value 100
score = 500;           // Changes 'score' variable only
console.log(`Score: ${score}, HighScore: ${highScore}`);
// Result: HighScore is still 100. They are independent.

// PART 2: The Object (Reference)
// Objects are "passed by reference".
const user = { name: "Alice", role: "Admin" };
const admin = user; // Copies the REFERENCE (The address in Heap)

console.log("\n[Before Mutation]");
console.log("User:", user);
console.log("Admin:", admin);

// MUTATION: Changing the data inside the house
console.log("\n[Mutating Admin...]");
admin.name = "Bob"; // I change 'admin', but 'user' also changes.

console.log("User:", user); // Alice became Bob?!
console.log("Admin:", admin);
console.log("Is User same object as Admin?", user === admin);

// PART 3: The "Const" Crash
console.log("\n[Attempting Reassignment...]");
try {
    // This fails because const protects the VARIABLE (the pointer), not the HOUSE.
    user = { name: "Charlie" };
} catch (error) {
    console.log("Error caught:", error.message);
}

console.log("--- EXPERIMENT END ---");