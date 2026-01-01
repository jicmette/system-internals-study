# Experiment: Strict Typing in Python
# Goal: Use Type Hints to prevent bugs before they happen.

from typing import List, Dict, Optional
from dataclasses import dataclass

print("--- EXPERIMENT START ---")

# 1. The "Loose" Way (Dictionary Hell)
# This is hard to maintain. What keys does 'user' have? Who knows?
def process_user_loose(user):
    name = user.get("name")
    age = user.get("age")
    # Bug Risk: What if 'emails' is missing? What if it's not a list?
    email = user["emails"][0].upper()
    return f"{name} ({age}) - {email}"

# 2. The "Strict" Way (Dataclasses + Typing)
# I define the SHAPE of our data clearly.

@dataclass
class UserStruct:
    name: str
    age: int
    emails: List[str]
    is_active: bool = True  # Default value

def process_user_strict(user: UserStruct) -> str:
    """
    Takes a UserStruct object and returns a formatted string.
    I know EXACTLY what fields exist.
    """
    if not user.emails:
        return f"{user.name} has no emails."

    primary_email = user.emails[0].upper()
    return f"{user.name} ({user.age}) - {primary_email}"

# --- TEST ---

# Data Source (Simulating API)
raw_data = {
    "name": "Alice",
    "age": 30,
    "emails": ["alice@example.com", "ali@work.com"]
}

# Loose Test
print("\n[Loose Mode]")
print(process_user_loose(raw_data))

# Strict Test
print("\n[Strict Mode]")
# I convert the raw dict into a structured object immediately.
# If data is missing (e.g., no age), this crashes HERE (good), not later (bad).
strict_user = UserStruct(
    name=raw_data["name"],
    age=raw_data["age"],
    emails=raw_data["emails"]
)

print(process_user_strict(strict_user))
print(strict_user)

# 3. The Safety Check (MyPy Simulation)
# If you uncomment the line below, a static analyzer (like MyPy) would scream errors.
# strict_user.age = "thirty"  # Error: Expected int, got str

print("--- EXPERIMENT END ---")