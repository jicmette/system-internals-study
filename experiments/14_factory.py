# Experiment: The Factory Pattern
# Goal: Decouple the logic of *creating* objects from *using* objects.

print("--- EXPERIMENT START ---")

# 1. The Interface (Abstract Base)
# All user types must follow this structure.
class User:
    def get_permissions(self):
        raise NotImplementedError("Subclasses must implement this.")

# 2. The Concrete Classes
class AdminUser(User):
    def get_permissions(self):
        return ["read", "write", "delete", "manage_users"]

class MemberUser(User):
    def get_permissions(self):
        return ["read", "write"]

class GuestUser(User):
    def get_permissions(self):
        return ["read_only"]

# 3. The Factory (The Creator)
class UserFactory:
    @staticmethod
    def create_user(user_type):
        """
        The Logic Center.
        Input: String ('admin', 'member', 'guest')
        Output: The correct User Object instance.
        """
        user_type = user_type.lower()

        if user_type == "admin":
            return AdminUser()
        elif user_type == "member":
            return MemberUser()
        elif user_type == "guest":
            return GuestUser()
        else:
            raise ValueError(f"Unknown user type: {user_type}")

# --- TEST ---

# Imagine this data comes from a database or API request
incoming_data = [
    "admin",
    "guest",
    "member",
    "ADMIN",
    "unknown hacker"
]

print("\n[Processing Logins...]")

for role in incoming_data:
    try:
        # The main code doesn't know about 'AdminUser' class.
        # It just asks the Factory.
        user = UserFactory.create_user(role)

        print(f"Role: {role.ljust(10)} | Permissions: {user.get_permissions()}")
        print(f"   -> Object Type: {type(user).__name__}")
        print(f"Memory Address: {hex(id(user))}")

    except ValueError as e:
        print(f"Error: {e}")

print("\n--- EXPERIMENT END ---")