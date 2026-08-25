# Python ATM Simulator

A simple console-based ATM system built in Python using Object-Oriented Programming (OOP). It allows a user to create a PIN, deposit and 
withdraw money, check their balance, and change their PIN through a text-based menu.

## Features

* 🔐 **Create PIN** — Set up a PIN on first use and save it to a local file.
* 💰 **Deposit** — Add money to the balance with PIN verification.
* 💵 **Withdraw** — Withdraw money with an insufficient-balance check.
* 📊 **Check Balance** — View the current balance after PIN verification.
* 🔁 **Change PIN** — Change the PIN after verifying the existing PIN.
* 🚪 **Exit** — Exit the program.

## How It Works

The `ATM` class stores the PIN in a local file called `ATM Data Base.txt`.

When the program starts, it reads the PIN from this file if a PIN has already been created. This allows the PIN to persist between program runs.

The balance is **not** saved to the file, so it resets to `0` whenever the program starts again.

## Requirements

* Python 3.x
* No external libraries are required.

## Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/RaoMohsin-hub/Python-ATM-Simulator.git
cd Python-ATM-Simulator
```

### 2. Run the program

```bash
python ATM.py
```

### 3. Follow the on-screen menu

```text
1. Enter 1 to create pin.
2. Enter 2 to deposit.
3. Enter 3 to withdraw.
4. Enter 4 to check balance.
5. Enter 5 to change pin.
6. Enter 6 to exit.
```

## Example

```text
Hello! How would you like to proceed?
1. Enter 1 to create pin.
2. Enter 2 to deposit.
3. Enter 3 to withdraw.
4. Enter 4 to check balance.
5. Enter 5 to change pin.
6. Enter 6 to exit.

Enter your choice: 1
Create pin: 1234
Pin Set Successfully.
```

## Project Files

* `ATM.py` — Main Python program containing the ATM system.
* `ATM Data Base.txt` — Local file used to store the PIN.

## Known Limitations

* The balance is not saved between sessions and resets to `0` when the program starts.
* Non-numeric input is not fully handled, so entering text where a number is expected may cause the program to crash.
* The PIN is stored as plain text and is not encrypted.
* This project is intended for learning purposes and is **not suitable for real-world banking or financial use**.

## Purpose

This project was created as a Python learning project to practice:

* Object-Oriented Programming
* Classes and objects
* Constructors
* Methods
* File handling
* User input
* Conditional statements
* Basic error checking

## Author

**Mohsin Raza**
