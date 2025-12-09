print("--- Memory Identity Experiment ---")

# CASE 1: Small Integers -5 to 256 (Cached by Python at startup)
a = 256
b = 256
print(f"\nComparing 256 is 256:")
print(f"Result: {a is b}")
print(f"Addresses: {hex(id(a))} vs {hex(id(b))}")

# CASE 2: Large Integers (Created fresh in the Heap)
x = 300
y = 300
print(f"\nComparing 300 is 300:")
print(f"Result: {x is y}")
print(f"Addresses: {hex(id(x))} vs {hex(id(y))}")