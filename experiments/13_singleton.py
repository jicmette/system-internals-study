# Experiment: The Singleton Design Pattern
# Goal: Ensure a class has only ONE instance (shared state).

import time

print("--- EXPERIMENT START ---")

class DatabaseConnection:
    _instance = None  # Class-level variable to hold the single instance

    def __new__(cls, db_name):
        """
        The Gatekeeper: Runs BEFORE __init__.
        It decides if I create a NEW object or return an OLD one.
        """
        if cls._instance is None:
            print(f"[Singleton] Creating NEW connection to {db_name}...")
            # Create the object using the parent (object) logic
            cls._instance = super(DatabaseConnection, cls).__new__(cls)

            # Simulate heavy connection time
            time.sleep(0.5)
            cls._instance.db_name = db_name
            cls._instance.status = "Connected"
        else:
            print(f"[Singleton] Returning EXISTING connection...")

        return cls._instance

    def query(self, sql):
        print(f"Running '{sql}' on {self.db_name} ({self.status})")

# --- TEST ---

print("\n1. Client A connects...")
db1 = DatabaseConnection("Vault0_DB")
print(f"DB1 Memory Address: {hex(id(db1))}")
db1.query("SELECT * FROM users")

print("\n2. Client B connects (tries to use same DB name)...")
db2 = DatabaseConnection("Vault0_DB")
print(f"DB2 Memory Address: {hex(id(db2))}")

print("\n3. Client C connects (tries to use DIFFERENT DB name)...")
# Crucial Check: Does it switch databases? Or reuse the old one?
db3 = DatabaseConnection("Testing_DB")
print(f"DB3 Memory Address: {hex(id(db3))}")
print(f"DB3 Name Property: {db3.db_name}")

print("\n4. Client D connects (tries to use DIFFERENT DB name)...")
# Crucial Check: Does it switch databases? Or reuse the old one?
db4 = DatabaseConnection("Ddata_DB")
print(f"DB4 Memory Address: {hex(id(db3))}")
print(f"DB4 Name Property: {db4.db_name}")

print("\n--- CHECK ---")
print(f"Are db1 and db2 the same? {db1 is db2}")
print(f"Are db1 and db3 the same? {db1 is db3}")
print(f"Are db1 and db4 the same? {db1 is db4}")

print("--- EXPERIMENT END ---")