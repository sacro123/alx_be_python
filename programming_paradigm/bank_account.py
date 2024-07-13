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
