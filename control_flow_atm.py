#!usr/bin/python3
def atm_machine():
    # Initial Setup
    balance = 5000
    pin = 1234
    attempts = 0
    max_attempts = 3
    total_deposits = 0
    total_withdrawals = 0

    # User Authentication
    while attempts < max_attempts:
        user_pin = int(input("Enter your PIN: "))
        if user_pin == pin:
            print("PIN accepted.")
            break
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempts left: {max_attempts - attempts}")
    else:
        print("Too many incorrect attempts. Access blocked.")
        return

    # Main Menu
    while True:
        print("\nMain Menu:")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            # Check Balance
            print(f"Your current balance is: ${balance}")

        elif choice == '2':
            # Deposit Funds
            deposit_amount = float(input("Enter amount to deposit: "))
            if deposit_amount > 0:
                balance += deposit_amount
                total_deposits += deposit_amount
                print(f"Deposited: ${deposit_amount}. New balance: ${balance}")
            else:
                print("Please enter a positive amount.")

        elif choice == '3':
            # Withdraw Funds
            withdraw_amount = float(input("Enter amount to withdraw: "))
            if withdraw_amount > 0:
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    total_withdrawals += withdraw_amount
                    print(f"Withdrew: ${withdraw_amount}. New balance: ${balance}")
                else:
                    print("Insufficient balance.")
            else:
                print("Please enter a positive amount.")

        elif choice == '4':
            # Change PIN
            current_pin = int(input("Enter your current PIN: "))
            if current_pin == pin:
                new_pin = input("Enter a new 4-digit PIN: ")
                if new_pin.isdigit() and len(new_pin) == 4:
                    pin = int(new_pin)
                    print("PIN changed successfully.")
                else:
                    print("New PIN must be a 4-digit integer.")
            else:
                print("Current PIN is incorrect.")

        elif choice == '5':
            # Exiting the ATM
            print("Thank you for using the ATM.")
            print(f"Total deposits made: ${total_deposits}")
            print(f"Total withdrawals made: ${total_withdrawals}")
            break

        else:
            print("Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    atm_machine()
