def calculator():
    print("Welcome to Simple Calculator!")
    print("Operations available:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("% : Modulus (Remainder)")
    print("^ : Exponentiation")
    print("Type 'quit' to exit")
    
    while True:
        try:
            # Get user input
            operation = input("\nEnter operation (+, -, *, /, %, ^) or 'quit': ").strip()
            
            if operation.lower() == 'quit':
                print("Thank you for using the calculator. Goodbye!")
                break
                
            if operation not in ['+', '-', '*', '/', '%', '^']:
                print("Invalid operation! Please choose from +, -, *, /, %, ^")
                continue
            
            # Get numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
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
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                else:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                    
            elif operation == '%':
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                else:
                    result = num1 % num2
                    print(f"{num1} % {num2} = {result}")
                    
            elif operation == '^':
                result = num1 ** num2
                print(f"{num1} ^ {num2} = {result}")
                
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Version with continuous calculations
def calculator_continuous():
    print("Welcome to Continuous Calculator!")
    print("Enter expressions like: 5 + 3, 10 * 2, etc.")
    print("Type 'quit' to exit")
    
    while True:
        try:
            expression = input("\nEnter expression: ").strip()
            
            if expression.lower() == 'quit':
                print("Thank you for using the calculator. Goodbye!")
                break
            
            # Parse the expression
            parts = expression.split()
            
            if len(parts) != 3:
                print("Invalid format! Use: number operator number (e.g., 5 + 3)")
                continue
                
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            # Perform calculation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            elif operator == '%':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 % num2
            elif operator == '^':
                result = num1 ** num2
            else:
                print(f"Invalid operator: {operator}")
                continue
            
            print(f"{expression} = {result}")
            
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    print("Select calculator mode:")
    print("1: Step-by-step calculator")
    print("2: Continuous expression calculator")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == '1':
        calculator()
    elif choice == '2':
        calculator_continuous()
    else:
        print("Invalid choice! Running step-by-step calculator.")
        calculator()
