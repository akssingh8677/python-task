# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Input: First number
    num1 = float(input("Enter first number: "))
    
    # Input: Second number
    num2 = float(input("Enter second number: "))
    
    # Input: Operation choice
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        result = add(num1, num2)
        operation = "Addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "Division"
    else:
        return "Invalid input! Please select a valid operation."
    
    # Output: Displaying the result
    print(f"{operation} of {num1} and {num2} is: {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()
