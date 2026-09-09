
class CellphoneLoadWallet:
    def __init__(self, name, mobileNumber, startingBalance):
        self.name = name
        self.mobileNumber = mobileNumber
        self.startingBalance = startingBalance

    def top_up(self, balance, topUpAmount):
        newBalance= balance + topUpAmount
        return newBalance
        

    def sendLoad(self, balance):
        self.receiverName = input("Enter receiver name: ")
        while True:
            self.receiverNumber = input("Enter mobile number: ")

            if self.receiverNumber.isdigit() and len(self.receiverNumber) == 11 and self.receiverNumber.startswith("09"):
                break
            else:
                print("Invalid mobile number. Please enter an 11-digit number starting with 09.")
        self.loadAmount = int(input("Enter load amount: "))

        if self.loadAmount > balance:
            print("Insufficient Balance. Please Top Up.")
            return balance
        else:
            newBalance= balance - self.loadAmount
            print(f"{self.loadAmount} load successfully sent to {self.receiverName} - {self.receiverNumber}. ")
            print(f"Your new balance is now Php {newBalance}.")
            return newBalance

    def sendLoad_wFee(self, balance):
        self.receiverName = input("Enter receiver name: ")
        while True:
            self.receiverNumber = input("Enter mobile number: ")

            if self.receiverNumber.isdigit() and len(self.receiverNumber) == 11 and self.receiverNumber.startswith("09"):
                break
            else:
                print("Invalid mobile number. Please enter an 11-digit number starting with 09.")
        self.loadAmount = int(input("Enter load amount: "))

        if self.loadAmount + 10 > balance:
            print("Insufficient Balance. Please Top Up.")
            return balance
        else:
            newBalance= balance - (self.loadAmount + 10)
            print(f"{self.loadAmount } load successfully sent to {self.receiverName} - {self.receiverNumber} with Php 10 network fee. ")
            print(f"Your new balance is now Php {newBalance}.")
            return newBalance


    def showBalance(self, balance):
        print(f"Owner Name: {self.name}")
        print(f"Mobile Number: {self.mobileNumber}")
        print(f"Balance: {balance}")


