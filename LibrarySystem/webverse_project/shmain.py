balance = 0.00   

def deposit(amount):
    global balance
    if amount <= 0:
        print("Amount must be positive.")
        return
    balance = balance + amount
    print(f"Deposited: {amount}")
    print(f"New balance: {balance}")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("Amount must be positive.")
        return
    if amount > balance:
        print("Insufficient balance. Transaction cancelled.")
        return
    balance = balance - amount
    print(f"Withdrawn: {amount}")
    print(f"New balance: {balance}")

def check_balance():
    global balance
    print(f"Current balance: {balance}")

def main():
    while True:
        print("\n 44 Bank Account Menu ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            withdraw(amount)

        elif choice == "3":
            check_balance()

        elif choice == "4":
            print("Exiting. Goodbye!")
            break  

        else:
            print("Invalid choice. Please select 1-4.")

main()