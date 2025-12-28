# Experiment: Python Decorators
# Goal: Write a wrapper that times execution without changing the original function.

import time
import functools

print("--- EXPERIMENT START ---")

# 1. The Decorator Definition
# A decorator is a function that takes a function as input...
# ...and returns a NEW function (the wrapper).
def timer(func):
    """Prints how long a function took to run."""
    @functools.wraps(func) # Preserves the name/docstring of the original function
    def wrapper(*args, **kwargs):
        print(f"\n[Timer] Starting {func.__name__}...")
        start_time = time.perf_counter()

        # Run the actual function
        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"[Timer] Finished {func.__name__} in {duration:.4f} seconds. Docstring: {func.__doc__}" )

        return result

    return wrapper

# 2. Applying the Decorator
# This is equivalent to: expensive_task = timer(expensive_task)
@timer
def expensive_task(seconds):
    """Simulates a heavy workload."""
    print(f"Working for {seconds} seconds...")
    time.sleep(seconds)
    return "Done!"

@timer
def quick_math(a, b):
    """Does simple math instantly."""
    return a + b

@timer
def subtraction(a, b):
  """Does subtraction of numbers."""
  return a - b

# 3. Testing
# Notice I just call them normally. The @timer handles the rest.
print("--- Test 1: Heavy Task ---")
result1 = expensive_task(1.5)
print(f"Result: {result1}")

result2 = expensive_task(5)
print(f"Result 5 seconds: {result2}")

print("\n--- Test 2: Quick Math ---")
result2 = quick_math(50, 100)
print(f"Result: {result2}")
print(f"Result 2: {quick_math(400, 5490)}")
sub = subtraction(1000, 500)
print(f"Result 3: {sub}")

# 4. Proof of Metadata Preservation
# Without @functools.wraps, this would print 'wrapper' instead of 'expensive_task'.
print("\n--- Introspection ---")
print(f"Function Name: {expensive_task.__name__}")
print(f"Docstring: {expensive_task.__doc__}")

print("\n------------------")
print(f"Function Name: {quick_math.__name__}")
print(f"Docstring: {quick_math.__doc__}")

print("\n------------------")
print(f"Function Name: {subtraction.__name__}")
print(f"Docstring: {subtraction.__doc__}")

print("--- EXPERIMENT END ---")