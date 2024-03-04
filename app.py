from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from decimal import Decimal


class cardHolder:
    def __init__(self, cardNum, pin, firstName, lastName, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstName = firstName
        self.lastName = lastName
        self.balance = Decimal(balance)  # Convert balance to Decimal

    # Other methods...


app = Flask(__name__)

# MySQL connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'sqlbibi',
    'database': 'atm'
}

# Function to retrieve card holder data from MySQL
def retrieve_card_holder(card_number):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Execute SQL query to retrieve card holder data by card number
        cursor.execute("SELECT * FROM CardHolder WHERE card_number = %s", (card_number,))
        card_holder_data = cursor.fetchone()

        conn.close()

        return card_holder_data
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    card_number = request.form['card_number']
    pin = request.form['pin']

    # Authenticate user using card number and pin
    card_holder = retrieve_card_holder(card_number)
    if card_holder and card_holder[1] == int(pin):
        return render_template('dashboard.html', holder=card_holder)
    else:
        return 'Invalid card number or pin'


@app.route('/create_account', methods=['POST'])
def create_account():
    # Handle account creation form submission
    card_number = request.form['card_number']
    pin = request.form['pin']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    balance = request.form['balance']
    
    # Perform database operations to save the new account data
    
    return 'Account created successfully'  # You

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        card_number = request.form['card_number']
        deposit_amount = Decimal(request.form['deposit_amount'])

        # Retrieve current balance
        card_holder = retrieve_card_holder(card_number)
        current_balance = card_holder[4]

        # Calculate new balance after deposit
        new_balance = current_balance + deposit_amount

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Update balance in the database
            cursor.execute("UPDATE CardHolder SET balance = %s WHERE card_number = %s", (new_balance, card_number))
            conn.commit()

            conn.close()

            return redirect(url_for('dashboard'))
        except mysql.connector.Error as e:
            print("Error connecting to MySQL:", e)
            return 'Error occurred while depositing amount'
    else:
        return render_template('deposit.html')

@app.route('/withdraw', methods=['GET','POST'])
def withdraw():
    card_number = request.form['card_number']
    withdraw_amount = Decimal(request.form['withdraw_amount'])

    # Retrieve current balance
    card_holder = retrieve_card_holder(card_number)
    current_balance = card_holder[4]

    # Check if withdrawal amount exceeds balance
    if withdraw_amount > current_balance:
        return 'Insufficient balance'

    # Calculate new balance after withdrawal
    new_balance = current_balance - withdraw_amount

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Update balance in the database
        cursor.execute("UPDATE CardHolder SET balance = %s WHERE card_number = %s", (new_balance, card_number))
        conn.commit()

        conn.close()

        return redirect(url_for('dashboard'))
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return 'Error occurred while withdrawing amount'

@app.route('/check_balance', methods=['POST'])
def check_balance():
    card_number = request.form['card_number']

    # Retrieve current balance
    card_holder = retrieve_card_holder(card_number)
    current_balance = card_holder[4]

    return f'Your current balance is: ${current_balance}'

if __name__ == '__main__':
    app.run(debug=True)
