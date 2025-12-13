# 02_mutable_defaults.py
# Experiment: The "Mutable Default Argument" Trap
# Goal: Show that default arguments are evaluated ONCE at definition time, not runtime.

print("--- EXPERIMENT START ---")

def add_student(name, class_list=[]):
    """
    Adds a student to a class list.
    If no list is provided, it starts a new one... OR DOES IT?
    """
    class_list.append(name)
    return class_list

# Scenario 1: I start a Math class
math_class = add_student("Alice")
print(f"Math Class: {math_class}")
# Expected: ['Alice']
# Actual:   ['Alice']

# Scenario 2: I start a History class (I expect a NEW empty list)
history_class = add_student("Bob")
print(f"History Class: {history_class}")
# Expected: ['Bob']
# Actual:   Wait... why is Alice here?

# Scenario 3: Let's check the memory address
print(f"\nMath List ID:    {hex(id(math_class))}")
print(f"History List ID: {hex(id(history_class))}")

print("\nCONCLUSION: The default list [] was created only once when Python read the 'def' line.")
print("--- EXPERIMENT END ---")

print("---------------------------------------------------")
print("\nFIXED CODE")

def add_student_fixed(name, class_list=None):
  """
  The Correct Pattern:
  I use None (immutable) as the default.
  I check for it inside the function
  """
  if class_list is None:
    class_list = []
  class_list.append(name)
  return class_list

science_class = add_student_fixed("Einstein")
print(f"\nScience Class: {science_class}")

art_class = add_student_fixed("Picasso")
print(f"Art Class: {art_class}")

print(f"\nScience ID: {hex(id(science_class))}")
print(f"Art ID: {hex(id(art_class))}")

print("\nCONCLUSION: The default list is set to None as default (Definition Time), and a new list is created each time the function is called (Runtime).")
print("--- EXPERIMENT END ---")