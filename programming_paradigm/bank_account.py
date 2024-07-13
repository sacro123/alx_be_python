class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

if __name__ == "__main__":
    # This block can be used for manual testing
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    account.display_balance()
    import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        if account.deposit(amount):
            print(f"Deposited: ${amount}")
        else:
            print("Deposit failed. Amount must be positive.")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid amount.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
