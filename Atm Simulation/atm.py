class ATM:
    def __init__(self, pin, balance=0):
        self.correct_pin = pin
        self.balance = balance
        self.authenticated = False

    def login(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.correct_pin:
                self.authenticated = True
                print("Login successful.\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. Attempts left: {attempts}")
        print("Too many failed attempts. Exiting.")
        return False

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}\n")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount <= 0:
                print("Please enter a positive amount.\n")
                return
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= 0:
                print("Please enter a positive amount.\n")
                return
            if amount > self.balance:
                print("Insufficient funds.\n")
                return
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    def menu(self):
        if not self.authenticated:
            return

        while True:
            print("----- ATM Menu -----")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Try again.\n")


# --- Run the ATM ---
if __name__ == "__main__":
    atm = ATM(pin="1234", balance=1000.0)  # Default PIN and balance
    if atm.login():
        atm.menu()
