// First: Priority 1 - Call Stack (Main Thread) - Synchronous
console.log("1. Script Start");

// Fourth: Priority 3 - Macrotask Queue (Slow lane) - Asynchronous
setTimeout(() => {
    console.log("2. setTimeout");
}, 0);

// Third: Priority 2 - Microtask Queue (VIP lane) - Asynchronous
Promise.resolve().then(() => {
    console.log("3. Promise 1");
}).then(() => {
    console.log("4. Promise 2");
});

// Second: Priority 1 - Call Stack (Main Thread) Synchronous
console.log("5. Script End");