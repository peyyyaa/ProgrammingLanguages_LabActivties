from CellphoneLoadWallet import CellphoneLoadWallet

name = input("Enter owner name: ")
while True:
    mobileNumber = input("Enter mobile number: ")

    if mobileNumber.isdigit() and len(mobileNumber) == 11 and mobileNumber.startswith("09"):
        break
    else:
        print("Invalid mobile number. Please enter an 11-digit number starting with 09.")
balance = int(input("Enter starting balance: "))
print("_________________________________\n")

myWallet = CellphoneLoadWallet(name, mobileNumber, balance)

repeat = True

while(repeat == True):
    print("————————————— MENU ——————————————")
    print("1. Top up Load" 
        "\n2. Send Load (same Network)" \
        "\n3. Send Load (other Network, with fee)" \
        "\n4. Show Balance" \
        "\n5. Exit")

    choice = int(input("Choose and option(1-5): "))
    
    print("_________________________________\n")

    if choice == 1:
        topUpAmount = int(input("Enter top-up amount: "))
        newBalance = myWallet.top_up(balance, topUpAmount)
        print(f"New Balance: {newBalance}") 
        balance = newBalance

    elif choice == 2:
        newBalance = myWallet.sendLoad(balance)
        balance = newBalance
    elif choice ==3:
        newBalance = myWallet.sendLoad_wFee(balance)
        balance = newBalance
    elif choice == 4:
        myWallet.showBalance(balance)
    elif choice == 5:
        print(f"Exiting Cellphone Load Wallet. Thank You {name}!")
        repeat = False
    else:
        print("Invalid Choice. Please enter a number from 1-5.")








