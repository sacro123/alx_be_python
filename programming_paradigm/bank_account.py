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
        print(f"Current balance: ${self._account_balance:.2f}")
     if __name__ == "__main__":
