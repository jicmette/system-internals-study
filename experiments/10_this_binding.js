'use strict';
// 10_this_binding.js
// Experiment: The 4 Rules of 'this'
// Goal: Show how 'this' changes based on the call site.

console.log("--- EXPERIMENT START ---");

// 1. The Object
const wizard = {
    name: "Gandalf",
    health: 100,
    heal: function(amount) {
        this.health += amount;
        console.log(`${this.name} has ${this.health} HP.`);
    }
};

const goblin = {
    name: "Goblin",
    health: 50,
};

const elf = {
    name: "Legolas",
    health: 76,
};

// 2. Implicit Binding (The Standard Way)
// Rule: Look to the left of the dot.
console.log("\n[1] IMPLICIT BINDING (wizard.heal)");
wizard.heal(10); // 'this' is wizard.

// 3. Losing Binding (The Trap)
// I steal the function reference. This will lose the connection to the wizard object.
const stealHeal = wizard.heal;

console.log("\n[2] LOST BINDING (stealHeal)");
try {
    stealHeal(10);
    // ERROR in strict mode (or undefined/NaN in loose mode).
    // Why? Because there is no dot! 'this' is global/undefined.
} catch (e) {
    console.log("Error:", e.message);
}

// 4. Explicit Binding (call/apply/bind)
// I force 'this' to be the goblin.

console.log("\n[3] EXPLICIT BINDING (.call)");
// call(thisArg, arg1, arg2...)
// "Run the wizard's code, but pretend 'this' is the goblin."
wizard.heal.call(goblin, 20);
wizard.heal.call(elf, 40);

console.log("\n[4] EXPLICIT BINDING (.apply)");
// apply(thisArg, [argsArray])
// Same as call, but takes an array of arguments.
wizard.heal.apply(goblin, [30]);
wizard.heal.apply(elf, [40, 20, 20]); // This will not work, it will only accept the first index in the list, due that the heal function accepts just one argument.

console.log("\n[5] HARD BINDING (.bind)");
// bind() returns a NEW function that is permanently locked to goblin.
const goblinHeal = wizard.heal.bind(goblin);
goblinHeal(50); // It works even without the dot.

const elfHeal = wizard.heal.bind(elf);
elfHeal(60);

console.log("--- EXPERIMENT END ---");