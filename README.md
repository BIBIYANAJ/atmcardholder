# ATM Card Holder System

This project is a simple ATM card holder system implemented in Python using Flask and MySQL. It allows users to perform basic ATM actions such as depositing money, withdrawing money, and checking their account balance.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Users can log in using their card number and pin.
- **Deposit**: Users can deposit money into their account.
- **Withdraw**: Users can withdraw money from their account.
- **Check Balance**: Users can check their account balance.
- **Create Account**: New users can create an account with a card number, pin, first name, last name, and initial balance.
- **MySQL Database**: The application uses a MySQL database to store user account information.

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/BIBIYANAJ/atmcardholder.git
   ```
1. Install the required dependencies:
 ```bash
pip install -r requirements.txt
```
2. Set up a MySQL database and update the database configuration in 'app.py' with your database credentials
3. Run the Flask application by executing the 'app.py' file:
```bash
python app.py
```
4. Access the application in your web browser at 'http://localhost:5000'.

## Usage
- Access the application in your web browser.
- Log in using your card number and pin.
- Perform actions such as depositing, withdrawing, or checking your balance.

## Technologies Used
- Python
- Flask
- MySQL

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or create a pull request.

## License
This project is licensed under the terms of the MIT license.

## Author
Bibiyana J
