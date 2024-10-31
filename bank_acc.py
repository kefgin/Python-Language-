class BankAccount:
    def __init__(self, account_id, password, balance=0):
        self.account_id = account_id
        self.password = password
        self.balance = balance
        self.transaction_history = []

    def login(self, entered_id, entered_password):
        if self.account_id == entered_id and self.password == entered_password:
            print("Login successful!")
            return True
        else:
            print("Invalid ID or Password.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

# Main flow
account = BankAccount(account_id="12345", password="pass123", balance=1000)

# Simulate Login
entered_id = input("Enter Account ID: ")
entered_password = input("Enter Password: ")
if account.login(entered_id, entered_password):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transaction History\n5. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            account.check_balance()
        elif choice == 4:
            account.show_transaction_history()
        elif choice == 5:
            print("Exiting. Thank you for using our service!")
            break
        else:
            print("Invalid option. Please try again.")
