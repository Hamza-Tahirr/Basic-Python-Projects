#Defining a funtion for depositing the money
def money_deposit():
    while True:
        amount = input("Enter the money you would like to deposit : RS.")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter amount greater than 0")
        else:
            print("Enter amount number only")

    return amount            
         
money_deposit()