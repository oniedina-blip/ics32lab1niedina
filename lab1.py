def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*' or operator == 'x':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"

def main():
    keep = 'y'
    
    while keep.lower() == 'y':
        print("\nWelcome to the ICS 32 PyCalc")
        print("Instructions: Enter two numbers and an operator (+, -, *, /)")

        try:
            val1 = float(input('Enter your first operand: '))
            val2 = float(input('Enter your second operand: '))
            operatorq = input('Enter your desired operator (+, -, *, /): ')
            
            result = calculate(val1, val2, operatorq)
    
            if isinstance(result, (int, float)):
                print(f"The result of your calculation is: {result:g}")
            else:
                print(result)
                
        except ValueError:
            print('Error: Please enter valid numbers.')

        keep = input("\nDo you want to run another calculation? (y/n): ")

if __name__ == "__main__":
    main()
