def withdraw():
    try:
        amount = int(input("Enter the amount you want to withdraw: R"))

        if amount > balance:
            print("Insufficient balance to make a withdrawal!")
            print(f"Current balance is R{balance}.")
            return 0

        elif amount < 10:
            print("You can't make a withdrawal of less than R10.")
            return 0

        else:
            print(f"You have successfully withdrawn R{amount}.")
            return amount

    except ValueError:
        print("Please enter a valid number.")
        return 0


def deposit():
    try:
        amount = int(input("Enter the amount you want to deposit: R"))

        if amount <= 0:
            print("You must deposit an amount greater than R0.")
            return 0

        print(f"You have successfully made a deposit of R{amount}.")
        return amount

    except ValueError:
        print("Please enter a valid number.")
        return 0


def view():
    print(f"Your current balance is R{balance}.")


balance = 0
pin = 65876
attempts = 0
logged_in = False
def main():
    global attempts, balance, logged_in
    while attempts < 3 and not logged_in:

        try:
            user_pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Please enter a valid PIN.")
            continue
        attempts += 1

        if user_pin == pin:
            logged_in = True
            print("Login successful!")

        else:
            if attempts < 3:
                print("Wrong PIN! Try again.")
            else:
                print("You have entered the wrong PIN 3 times.")
                print("Your card has been blocked.")


    while logged_in:

        print("Please select one of the options below:")
        print("1. View balance")
        print("2. Withdraw")
        print("3. Make a deposit")
        print("4. Exit")

        try:
            selection = int(input("Select an option: "))
        except ValueError:
            print("Please enter a number from 1 to 4.")
            continue

        if selection == 1:
            view()

        elif selection == 2:
            balance-=withdraw()

        elif selection == 3:
            balance+=deposit()

        elif selection == 4:
            print("Goodbye! Have a lovely day.")
            logged_in = False

        else:
            print("Invalid selection. Please choose an option from 1 to 4.")

if __name__=="__main__":
   main()