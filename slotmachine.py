# Defining global constant that is maximum number of lines to bet on
MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1

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

#For betting on number of lines 
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? : ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Enter number only")

    return lines  




def main():         
    balance = money_deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()    