import mysql.connector
from decimal import Decimal
def insert_card_holder(conn, card_number, pin, first_name, last_name, balance):
    try:
        cursor = conn.cursor()

        # SQL query to insert a new card holder into the table
        insert_query = "INSERT INTO CardHolder (card_number, pin, first_name, last_name, balance) VALUES (%s, %s, %s, %s, %s)"
        
        # Data tuple containing values for insertion
        data = (card_number, pin, first_name, last_name, balance)

        # Execute the insert query with the provided data
        cursor.execute(insert_query, data)

        # Commit changes to the database
        conn.commit()

        # Close cursor
        cursor.close()

        print("New card holder added successfully.")
    except mysql.connector.Error as e:
        print("Error inserting new card holder:", e)

def get_user_input(prompt):
    # Function to get user input with error handling
    while True:
        try:
            user_input = input(prompt)
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sqlbibi",
            database="atm"
        )

        # Get input values from the user
        card_number = get_user_input("Enter card number: ")
        pin = int(get_user_input("Enter PIN: "))
        first_name = get_user_input("Enter first name: ")
        last_name = get_user_input("Enter last name: ")
        balance = Decimal(get_user_input("Enter balance: "))

        # Insert new card holder into the database
        insert_card_holder(conn, card_number, pin, first_name, last_name, balance)

        # Close connection
        conn.close()
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)

if __name__ == "__main__":
    main()
