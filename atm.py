class ATM:

    def __init__(self):
        self.pin = ""
        self.balance = 10000
        self.menu()

    def menu(self):

        while True:

            print("\n====== ATM MENU ======")
            print("1. Create PIN")
            print("2. Change PIN")
            print("3. Check Balance")
            print("4. Exit")

            user_input = input("Enter your choice: ")

            if user_input == "1":
                self.create_pin()

            elif user_input == "2":
                self.change_pin()

            elif user_input == "3":
                self.check_balance()

            elif user_input == "4":
                print("Thank You!")
                break

            else:
                print("Invalid Option! Try Again.")

    def create_pin(self):

        user_pin = input("Enter New PIN: ")
        self.pin = user_pin

        print("✅ PIN Created Successfully")

    def change_pin(self):

        old_pin = input("Enter Old PIN: ")

        if self.pin == old_pin:

            new_pin = input("Enter New PIN: ")
            self.pin = new_pin

            print("✅ PIN Changed Successfully")

        else:
            print("❌ Wrong PIN")

    def check_balance(self):

        user_pin = input("Enter PIN: ")

        if user_pin == self.pin:

            print("💰 Balance is:", self.balance)

        else:
            print("❌ Wrong PIN")


obj = ATM()
