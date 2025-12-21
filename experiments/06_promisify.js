// Goal: Convert a "Callback" function into a "Promise" function.

const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'secret.txt');

// 1. The Old Way (Callback Hell)
// I pass a function (err, data) that runs "whenever it finishes".
console.log("--- Reading File (Old Way) ---"); // Synchronous

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error("Old Way Error:", err);
    } else {
        console.log("Old Way Data:", data);
    }
});

// 2. The New Way (Promisify Wrapper) - The Bridge
// I create a function that returns a Promise.
function readFilePromise(path) {
    return new Promise((resolve, reject) => {
        // Inside here, I run the old code.
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                // Instead of console.error, I REJECT the ticket.
                reject(err);
            } else {
                // Instead of console.log, I RESOLVE the ticket with data.
                resolve(data);
            }
        });
    });
}

// 3. Consuming the Promise (Clean Chain) - The Present
console.log("\n--- Reading File (New Way) ---"); // Synchronous
readFilePromise(filePath)
    .then((data) => {
        console.log("New Way Data:", data);
        return data.toUpperCase(); // Uppercase
    })
    .then((upperData) => {
        console.log("UPPERCASE:", upperData);
        return upperData.toLowerCase(); // Lowercase
    })
    .then((lowerData) => {
        console.log("lowercase:", lowerData);
    })
    .catch((err) => {
        console.error("Promise Error:", err);
    });

// 4. The Modern Way (Async/Await) - The Future
console.log("\n--- Reading File (Async/Await) ---"); // Synchronous

async function run() {
    try {
        // I "await" the promise. JS pauses here until it resolves.
        const data = await readFilePromise(filePath);
        console.log("Modern Data:", data);

        const upperData = data.toUpperCase();
        console.log("Modern Transformed:", upperData);

    } catch (err) {
        // I use standard try/catch instead of .catch()
        console.error("Modern Error:", err);
    }
}

run();