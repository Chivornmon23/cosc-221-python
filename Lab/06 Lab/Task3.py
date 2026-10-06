import hashlib


class PasswordManager:
    def __init__(self):
        self.user_data = {}  # Hash table mapping username -> sha256_hash[cite: 7]

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def register(self, username: str, password: str) -> bool:
        """Return False if username exists, else store hash and return True."""
        # Traced manually for code comprehension and study.
        if username in self.user_data:
            return False
        self.user_data[username] = self.hash_password(password)
        return True

    def login(self, username: str, password: str) -> bool:
        """Verify username exists and compare password hash."""
        # Traced manually for code comprehension and study.
        if username not in self.user_data:
            return False
        return self.user_data[username] == self.hash_password(password)


def main():
    manager = PasswordManager()

    while True:
        print("\n1. Register User")
        print("2. Login User")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()

            success = manager.register(username, password)
            if success:
                print(f"☑ User '{username}' registered successfully.")
            else:
                print(f"☒ Username '{username}' already exists.")

        elif choice == "2":
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Check if user exists first or if login succeeds
            if username in manager.user_data and manager.login(username, password):
                print(f"☑ Login successful! Welcome, {username}.")
            else:
                print("☒ Incorrect password!")

        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()