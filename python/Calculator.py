def calculator():
    # Get first number from user
    num1 = float(input("Enter the first number: "))
    
    # Get second number from user
    num2 = float(input("Enter the second number: "))
    
    # Get operation from user
    print("\nAvailable operations:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    operation = input("\nEnter the operation you want to perform: ")
    
    # Perform calculation based on operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        # Check for division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation! Please use +, -, *, or /")

# Run the calculator
if __name__ == "__main__":
    calculator()