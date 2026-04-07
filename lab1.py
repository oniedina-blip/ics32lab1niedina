def calculate(num1, num2, operator):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    if num2 != 0:
      return num1 / num2
    else:
      return "Error: Division by zero"
  else:
    return 'Invalid operator.'

def main():
  print('Welcome to the ICS 32 PyCalc')
  print('Please enter two numbers and an operator (+, -, *, /)')

  try:
    val1 = float(input('Enter your first operand: '))
    val2 = float(input('Enter your second operand: '))
    operatorq = input('Enter your desired operator (+, -, *, /): ')

    result = calculate(val1, val2, operatorq)
    print(f"\nThe result of your calculation is: {int(result)}")
  except ValueError:
    print('Error: Please enter valid numbers.')
if __name__ == "__main__":
  main()
