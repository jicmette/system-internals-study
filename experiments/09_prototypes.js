// 09_prototypes.js
// Goal: Understand the Prototype Chain (The "Delegation" Model).

console.log("--- EXPERIMENT START ---");

// 1. The Parent "Class" (Constructor Function)
function Animal(name, food) {
    this.name = name;
    this.food = food;
}

// Add a method to the Parent's Prototype
// This method is NOT copied to every animal. It lives in one place.
Animal.prototype.speak = function() {
    return `${this.name} makes a noise.`;
};

Animal.prototype.runs = function(){
    return `${this.name} runs in the park!`
};

// 2. The Child "Class"
function Dog(name, food, breed) {
    // Call the Parent constructor (Super)
    Animal.call(this, name, food);
    this.breed = breed;
}

// 3. The Link (Inheritance)
// I tell Dog: "If you can't find a method, look at Animal."
// I use Object.create to make a clean link.
Dog.prototype = Object.create(Animal.prototype);

// Fix the constructor pointer (otherwise it points to Animal)
//Dog.prototype.constructor = Dog;

// Add a Child-specific method
Dog.prototype.bark = function() {
    return `${this.name} barks!`;
};

Dog.prototype.eats = function() {
    return `likes to eat ${this.food}`
}
// --- TEST ---
const doki = new Dog("Doki", "Meat", "Labrador");

console.log("1. Own Property:", doki.breed); // Found on Dog
console.log("2. Inherited Method:", doki.speak()); // Found on Animal.prototype
console.log("3. Child Method:", doki.bark()); // Found on Dog.prototype
console.log(`${doki.name} ${doki.eats()}`);

// PROOF: The Chain
console.log("\n--- The Chain Check ---");
console.log("Is myDog an instance of Dog?", doki instanceof Dog); // true
console.log("Is myDog an instance of Animal?", doki instanceof Animal); // true

// The "Secret" Link (__proto__)
// Node.js lets us inspect the prototype directly
console.log("Dog's Prototype is Animal?", Object.getPrototypeOf(Dog.prototype) === Animal.prototype);

console.log("--- EXPERIMENT END ---");