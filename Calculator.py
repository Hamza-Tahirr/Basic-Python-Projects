def calculator():
    while True:
        print("Enter 'quit' to exit the program.")
        num1 = input("Enter the first number: ")
        if num1 == 'quit':
            break
        num2 = input("Enter the second number: ")
        if num2 == 'quit':
            break
        operator = input("Enter the operator (+, -, *, /): ")
        if operator == 'quit':
            break
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: division by zero")
                continue
            result = num1 / num2
        else:
            print("Invalid operator. Please enter a valid operator.")
            continue
        print(f"{num1} {operator} {num2} = {result}\n")
