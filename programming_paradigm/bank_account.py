class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ${amount:.2f}")
            return True
        elif amount <= 0:
            print("Withdraw amount must be positive.")
            return False
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

if __name__ == "__main__":
    # This block can be used for testing the class manually
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    account.display_balance()
    import argparse
from bank_account import BankAccount

def main():
    parser = argparse.ArgumentParser(description="Bank Account Management")

    parser.add_argument("operation", choices=["deposit", "withdraw", "balance"], help="Banking operation to perform")
    parser.add_argument("amount", type=float, nargs="?", help="Amount for deposit or withdrawal")
    parser.add_argument("--initial_balance", type=float, default=0, help="Initial balance of the bank account")

    args = parser.parse_args()

    # Initialize the bank account
    account = BankAccount(args.initial_balance)

    # Perform the operation
    if args.operation == "deposit":
        if args.amount is not None:
            account.deposit(args.amount)
        else:
            print("Deposit amount not specified.")
    elif args.operation == "withdraw":
        if args.amount is not None:
            success = account.withdraw(args.amount)
            if not success:
                print("Withdrawal failed.")
        else:
            print("Withdraw amount not specified.")
    elif args.operation == "balance":
        account.display_balance()

    # Always display the balance after the operation
    if args.operation in ["deposit", "withdraw"]:
        account.display_balance()

if __name__ == "__main__":
    main()
    python main-0.py deposit 100 --initial_balance 200
    python main-0.py withdraw 50 --initial_balance 200
    python main-0.py balance --initial_balance 200
