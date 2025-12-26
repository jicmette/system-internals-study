# Experiment: Dunder Methods (Double Underscore)
# Goal: Make custom objects behave like built-in types (int, str, list).

print("--- EXPERIMENT START ---")

class Wallet:
    def __init__(self, owner, balance):
        """The Constructor: Runs when you create the object."""
        self.owner = owner
        self.balance = balance

    def __str__(self):
        """The String Representation: Runs when you call print(obj)."""
        return f"Wallet({self.owner}: ${self.balance})"

    def __add__(self, other):
        """The Addition Operator (+): Runs when you do obj1 + obj2."""
        if not isinstance(other, Wallet):
            return NotImplemented

        new_balance = self.balance + other.balance
        return Wallet("Joint Account", new_balance)

    # def __sub__(self, other)

    def __len__(self):
        """The Length Function: Runs when you call len(obj)."""
        # Let's say length represents the 'wealth level' (digits).
        return len(str(self.balance))

    def __eq__(self, other):
        """The Equality Operator (==): Runs when you do obj1 == obj2."""
        return self.balance == other.balance

# --- TEST ---

alice = Wallet("Alice", 50)
bob = Wallet("Bob", 150)
israel = Wallet("Israel", 200)

# 1. Testing __str__
print(f"\n[1] Printing Objects:")
print(alice)  # Uses __str__
print(bob)
print(israel)

# 2. Testing __add__
print(f"\n[2] Adding Wallets (+):")
merged = alice + bob + israel # Uses __add__ behind the scenes
print(f"Result: {merged}")

# 3. Testing __len__
print(f"\n[3] Wealth Level (len):")
print(f"Alice Wealth Level: {len(alice)}") # 2 (digits in 50)
print(f"Bob Wealth Level:   {len(bob)}")   # 3 (digits in 150)
print(f"Israel Wealth Level:   {len(israel)}")   # 3 (digits in 200)

# 4. Testing __eq__
# Are they the same object in the Heap?
print(f"\n[4] Equality Check (==):")
print(f"Is Alice equal to Bob? {alice == bob}")
print(f"Is Alice equal to Israel? {alice == israel}")

print("--- EXPERIMENT END ---")