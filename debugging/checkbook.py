#!/usr/bin/python3
"""
checkbook.py — A basic CLI checkbook application with error handling.
"""

class Checkbook:
    """A simple class to manage a user's checkbook balance."""

    def __init__(self):
        """Initialize a new checkbook with a balance of 0.0 dollars."""
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit the specified amount into the checkbook."""
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient balance is available."""
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Display the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """Main loop for interacting with the checkbook."""
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            break
        elif action in ['deposit', 'withdraw']:
            # Input validation for amount
            amount_str = input(f"Enter the amount to {action}: $")
            try:
                amount = float(amount_str)
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue

            if action == 'deposit':
                cb.deposit(amount)
            else:
                cb.withdraw(amount)

        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
