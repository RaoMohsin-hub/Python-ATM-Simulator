
class ATM:
    def __init__(self):
        with open("ATM Data Base.txt", "r") as f:
            data = f.read()
        
        if data.strip():
            self.pin = int(data)
        else:
            self.pin = None
        
        self.balance = 0

        self.menu()

    def menu(self):
        print("""
Hello! , How would like to proceed you ?
1. Enter 1 to create pin.
2. Enter 2 to deposit.
3. Enter 3 to withdraw
4. Enter 4 to check balance.
5. Enter 5 to change pin.
6. Enter 6 to exit.
""")
        while True:
            user_input = int(input("Enter your choice: "))
            if user_input == 1:
                self.create_pin()
            elif user_input == 2:
                self.deposit()
            elif user_input == 3:
                self.withdraw()
            elif user_input == 4:
                self.check_balance()
            elif user_input == 5:
                self.change_pin()
            elif  user_input == 6:
                break
            else:
                print("Invalid Choice")

    def create_pin(self):
        user = int(input("Create pin "))
        self.pin = user 
        with open("ATM Data Base.txt","w") as f:
            f.write(str(user) + "\n")

        print("Pin Set Successfully.")

    def deposit(self):
        temp = int(input("Enter your pin.... "))
        if temp == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance += amount
            print("Amount deposited.")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = int(input("Enter your pin... "))
        if temp == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Amount deducted seccessfuly.")
            else:
                print("Insufficient balance")
    

    def check_balance(self):
        temp = int(input("Enter your pin... "))
        if temp == self.pin:
            print("Your current balance is: ",self.balance)
        else:
            print("Invalid Pin")

    def change_pin(self):
        old_pin = self.pin
        new_pin = int(input("Enter your old pin.... "))
        if new_pin == old_pin:
            new_pin = int(input("Enter new pin. "))
            self.pin = new_pin
            print("Pin Changed Successfully.")
        else:
            print("Invlaid Old pin")
            

    

user1 = ATM()
