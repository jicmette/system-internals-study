// 05_promise_chain.js

console.log("1. App Started");

// Step 1: Simulate Logging In (Takes 1 second)
function loginUser(username) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(`2. Logged in as ${username}`);
            // Success! Pass the User ID to the next step
            resolve({ userId: 101 });
        }, 1000);
    });
}

// Step 2: Simulate Fetching Profile (Takes 1 second)
function getUserProfile(userId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(`3. Found profile for User ID: ${userId}`);
            // Success! Pass the Email to the next step
            resolve({ email: "israel@example.com" });
        }, 1000);
    });
}

// Step 3: Simulate Sending Email (Takes 0.5 seconds)
function sendEmail(email) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(`4. Email sent to ${email}`);
            reject("Error, email not sent. Task 4 pending.");
        }, 500);
    });
}

// --- THE CHAIN ---

loginUser("Israel")
    .then((userData) => {
        // 'userData' is what 'resolve' passed in Step 1
        return getUserProfile(userData.userId);
    })
    .then((profileData) => {
        // 'profileData' is what 'resolve' passed in Step 2
        return sendEmail(profileData.email);
    })
    .then(() => {
        console.log("5. All steps complete!");
    })
    .catch((error) => {
        console.log("🚨 SOMETHING WENT WRONG:");
        console.log(error)
    });

console.log("6. App waiting...");