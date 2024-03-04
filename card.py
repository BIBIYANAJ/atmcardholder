import mysql.connector
from cardHolder import cardHolder
from decimal import Decimal


class cardHolder:
    def __init__(self, cardNum, pin, firstName, lastName, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstName = firstName
        self.lastName = lastName
        self.balance = Decimal(balance)  # Convert balance to Decimal

    # Other methods...


def print_menu():
    print("Please choose from one of the following options...(type '1' or '2' or '3' or '4')")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit_amt = Decimal(input("How much money would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit_amt)
        print("Thank you for your deposit. Your new balance is: ", cardHolder.get_balance())
    except ValueError:
        print("Invalid Input")

def withdraw(cardHolder):
    try:
        withdraw_amt = Decimal(input("How much money would you like to withdraw: "))
        current_balance = cardHolder.get_balance()
        if current_balance < withdraw_amt:
            print("Insufficient balance :(")
        else:
            new_balance = current_balance - withdraw_amt
            cardHolder.set_balance(new_balance)
            print("You're good to go! Thank you :)")
    except ValueError:
        print("Invalid Input")


def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

def retrieve_card_holders():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sqlbibi",
            database="atm"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM CardHolder")
        card_holders_data = cursor.fetchall()

        card_holders = []
        for data in card_holders_data:
            card_holders.append(cardHolder(*data))

        conn.close()

        return card_holders
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None

if __name__ == "__main__":
    list_of_cardHolders = retrieve_card_holders()
    if list_of_cardHolders is None:
        exit()

    current_user = None

    while True:
        try:
            debit_card_num = input("Please insert your debit card: ")
            debit_match = [holder for holder in list_of_cardHolders if holder.cardNum == debit_card_num]
            if len(debit_match) > 0:
                current_user = debit_match[0]
                break
            else:
                print("Card number not recognized. Please try again.")
        except ValueError:
            print("Card number not recognized. Please try again.")

    while True:
        try:
            user_pin = int(input("Please enter your pin: ").strip())
            if current_user.get_pin() == user_pin:
                break
            else:
                print("Invalid pin. Please try again.")
        except ValueError:
            print("Invalid pin. Please try again.")

    print("Welcome", current_user.get_firstname(), ":)")

    while True:
        print_menu()
        try:
            option = int(input())
        except ValueError:
            print("Invalid input. Please try again.")

        if option == 1:
            deposit(current_user)
        elif option == 2:
            withdraw(current_user)
        elif option == 3:
            check_balance(current_user)
        elif option == 4:
            break
        else:
            print("Invalid option. Please try again.")

    print("Thank you. Have a nice day.")
