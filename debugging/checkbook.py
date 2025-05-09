#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        """Initialise le solde du compte à zéro"""
        self.balance = 0.0

    def deposit(self, amount):
        """Dépose un montant sur le compte"""
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Effectue un retrait si le solde est suffisant"""
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Affiche le solde actuel"""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """Fonction principale qui permet à l'utilisateur d'interagir avec le compte"""
    cb = Checkbook()
    while True:
        # Demander à l'utilisateur quelle action il souhaite effectuer
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                # Demander un montant et tenter de le convertir en nombre flottant
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'withdraw':
            try:
                # Demander un montant pour le retrait
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
