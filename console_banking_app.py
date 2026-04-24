class BankAccount:
    next_id = 1001

    def __init__(self):
        self.id = BankAccount.next_id
        BankAccount.next_id += 1

        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive!")

        self.balance += amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive!")

        if amount > self.balance:
            raise ValueError("Insufficient Balance!")

        self.balance -= amount
        self.transactions.append(f"Withdrawn {amount}")

    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Transfer target must be a BankAccount!")

        if other_account is self:
            raise ValueError("Cannot transfer to the same account!")

        if amount <= 0:
            raise ValueError("Amount must be positive!")

        if amount > self.balance:
            raise ValueError("Insufficient Balance!")

        self.balance -= amount
        other_account.balance += amount

        self.transactions.append(f"Transferred {amount} to Account {other_account.id}")
        other_account.transactions.append(f"Received {amount} from Account {self.id}")

    def check_balance(self):
        return self.balance

    def history(self):
        return self.transactions


# ---------------- MAIN SYSTEM ---------------- #

accounts = {}

while True:
    print("\n====== BANK MENU ======")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check Balance")
    print("6. Transaction History")
    print("7. Exit")

    choice = input("Enter choice: ")

    try:
        # Create Account
        if choice == "1":
            print(f"-"*50)
            acc = BankAccount()
            accounts[acc.id] = acc
            print(f"Account created successfully! ID: {acc.id}")

        # Deposit
        elif choice == "2":
            print(f"-"*50)
            acc_id = int(input("Enter account ID: "))
            amount = int(input("Enter amount: "))

            if acc_id not in accounts:
                print("Invalid account ID!")
                continue

            accounts[acc_id].deposit(amount)
            print("Deposit successful!")

        # Withdraw
        elif choice == "3":
            print(f"-"*50)
            
            acc_id = int(input("Enter account ID: "))
            amount = int(input("Enter amount: "))

            if acc_id not in accounts:
                print("Invalid account ID!")
                continue

            accounts[acc_id].withdraw(amount)
            print("Withdrawal successful!")

        # Transfer
        elif choice == "4":
            print(f"-"*50)
            
            from_id = int(input("From account ID: "))
            to_id = int(input("To account ID: "))
            amount = int(input("Enter amount: "))

            if from_id not in accounts or to_id not in accounts:
                print("Invalid account ID!")
                continue

            accounts[from_id].transfer(accounts[to_id], amount)
            print("Transfer successful!")

        # Check Balance
        elif choice == "5":
            print(f"-"*50)
            
            acc_id = int(input("Enter account ID: "))

            if acc_id not in accounts:
                print("Invalid account ID!")
                continue

            print(f"Balance: {accounts[acc_id].check_balance()}")

        # Transaction History
        elif choice == "6":
            print(f"-"*50)
            
            acc_id = int(input("Enter account ID: "))

            if acc_id not in accounts:
                print("Invalid account ID!")
                continue

            print("Transaction History:")
            for t in accounts[acc_id].history():
                print(t)

        # Exit
        elif choice == "7":
            print(f"-"*50)
            
            print("Exiting system...")
            break

        else:
            print(f"-"*50)
            
            print("Invalid choice!")

    except Exception as e:
        print("Error:", e)